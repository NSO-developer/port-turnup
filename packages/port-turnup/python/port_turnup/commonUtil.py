import ncs
import re
# class to be added..
class CommonUtil :
    
    def getDeviceType(self,service, device, name):
        device = device.ncs__devices.device[name]
        if(device.device_type.netconf.exists()):
            device_type = "netconf"
            return device_type
        if(device.device_type.cli.exists()):
            device_type = device.device_type.cli.ned_id
            service.log.debug("THE NED_ID CONTAINS >>>>>>>>>>"+device_type);
            return device_type

    def getInterfaceType(self, service, inp):
        inp = inp.lower()
        if inp.startswith("gi"):
            interface_type = "GigabitEthernet"
        elif inp.startswith("tengige"):
            interface_type = "TenGigE"
        elif inp.startswith("te"):
            interface_type = "TenGigabitEthernet"
        elif inp.startswith("be"):
            interface_type = "Bundle-Ether"
        elif inp.startswith("bundleether") or inp.startswith("bundle-ether"):
            interface_type = "Bundle-Ether"
        elif inp.startswith("portchannel") or inp.startswith("port-channel"):
            interface_type = "Bundle-Ether"
        elif inp.startswith("fastethernet"):
            interface_type = "FastEthernet"
        elif inp.startswith("ethernet"):
            interface_type = "Ethernet"
        elif inp.startswith("ethernet"):
            interface_type = "Ethernet"
        
        return interface_type

    def getInterfaceId(self, service, name,typ):
       if typ is "GigabitEthernet" or  "TenGigabitEthernet" or  "FastEthernet" or  "Ethernet" or  "TenGigE" :
           interface_split = name.split("/")
           service.log.debug("LENGTH OF SPLIT LIST IS "+str(len(interface_split)))

           patern = re.compile("[^0-9]+([0-9]+)$");
           result = patern.match(interface_split[0])
           if len(result.group(0)) is not 0 :
               interface_start = result.group(1)
               int_id = interface_start;
               for i in range(1,len(interface_split)):
                   if not len(interface_split[i]) is 0 :
                       int_id = int_id + "/" +interface_split[i]
       elif typ is "Bundle-Ether" :
           patern = re.compile("[^0-9]+([0-9]+)$");
           result = patrn.match(name)
           if len(result.group(0)) is not 0 :
               int_id = result.group(1)
       return int_id
