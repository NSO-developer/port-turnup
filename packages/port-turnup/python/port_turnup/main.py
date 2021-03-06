# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
from port_turnup.commonUtil import CommonUtil

class ServiceCallbacks(Service):

    # The create() callback is invoked inside NCS FASTMAP and
    # must always exist.
    @Service.create
    def cb_create(self, tctx, root, service, proplist):
        int_id = ""
        interface_type = ""
        cmnutil =  CommonUtil()
        self.log.debug('Service create(service=', service._path, ')')
        device_type = cmnutil.getDeviceType(self,root,service.device)
        vars = ncs.template.Variables()
        if "netconf" not in device_type:
            interface_type = cmnutil.getInterfaceType(self, service.interface)
            int_id = cmnutil.getInterfaceId(self, service.interface, interface_type)
        vars.add('INTID',int_id)
        vars.add('INTERFACE-TYPE',interface_type)
        template = ncs.template.Template(service)
        template.apply('port-turnup-template', vars)



# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #
        self.register_service('port-turnup', ServiceCallbacks)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
