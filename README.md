# Description

An atomic service required to configure physical ports on a router or switches. Port turnup service can configure various attributes for interfaces with description, mtu, duplex, speed and assign vlans to ports.


# Supported Device Types

Following device types have been validated & supported by the device onboarding framework.


| Device Type | Model   | NED          | NED version tested |
|-------------|---------|--------------|--------------------|
|Catalyst     | 4948    | cisco-ios    |       3.1.14       |
|Nexus        | 6k & 9k | cisco-nx     |       5.0.9        |
|Arista       | 7280se  | arista-dcs   |       4.3.1        |
|Juniper      | ex4550  | juniper-junos|       3.0.35       |
|ASR9K        | 9001    | cisco-iosxr  |       5.0.10       |

# Author
**syellabo**


# Version
1.1

# Release Date
29 - November - 2018

# Installation

* Place the downloaded package in packages directory located in nso run directory.
* Package has been tested with NSO-4.3.1 and python 3.5.2.
* Make and Reload the packages.
* For executing the portturnup package in NSO-4.3.1 and python 3.5.2, user must create a symlink to `_ncs_py3.cpython-33m.so` `_ncs_py3` as shown below :

```
cisco@dev-service-node:/opt/ncs/current/src/ncs/pyapi/_ncs$ ln -s _ncs_py3.cpython-33m.so _ncs_py3.so
```

# Create Netsim devices

1.  Go to nso run directory after placing required NED packages in packages directory

2. Create required netsim devices using below commands

       $ ncs-netsim create-network packages/cisco-ios 2 ios_
       DEVICE ios_0 CREATED
       DEVICE ios_1 CREATED
       $ ncs-netsim add-to-network packages/juniper-junos 2 junos_
       DEVICE junos_0 CREATED
       DEVICE junos_1 CREATED
       $ ncs-netsim add-to-network packages/arista-dcs 2 arista_
       DEVICE arista_0 CREATED
       DEVICE arista_1 CREATED
       $ ncs-netsim add-to-network packages/cisco-nx 2 nx_
       DEVICE nx_0 CREATED
       DEVICE nx_1 CREATED
       $ ncs-netsim add-to-network packages/cisco-iosxr 2 iosxr_
       DEVICE iosxr_0 CREATED
       DEVICE iosxr_1 CREATED

3. Start Netsim devices

       ncs-netsim start

4. Using command below, create XML file containing information about newly created netsim devices

       ncs-netsim ncs-xml-init > netsim-devices.xml

5. Add default authgroup (if it doesn't exist) for devices in NSO

       admin@ncs% set devices authgroups group default default-map remote-name admin remote-password admin
       [ok]
       [edit]
       admin@ncs% commit
       Commit complete.
       [ok]
       [edit]
       admin@ncs%

6. Load the XML file created in step 4 so that netsim devices information can be imported into NSO

       ncs_load -l -m netsim-devices.xml

# Usage

**Cisco Access Port:**

`set services port-turnup ios_1 gigabitethernet0/0 port-type access-port description connected-to-web-server mtu 1480 vlan-id 30`


**Cisco Trunk Port:**

`set services port-turnup ios_1 gigabitethernet0/1 port-type trunk-port description connected-to-gateway-server vlan-ids 50,60 mtu 1480`


**Juniper Access-Port:**

`set services port-turnup junos_0 xe0/0 port-type access-port description connected-to-DB vlan-name db-vlan vlan-id 40 mtu 1480`


**Juniper Trunk-Port:**

`set services port-turnup junos_0 xe0/1 port-type trunk-port description connected-to-gateway vlan-ids 70,80 mtu 1480`


**Cisco iosXR Access-Port:**

`set services port-turnup iosxr_0 GigabitEthernet0/0/0/1 description test mtu 4484 port-type access-port vlan-id 112`

# Note

Please note that this package needs NEDs for all supported device types as mentioned in section "Supported Device Types" above. If you don't have one of these NEDs then please comment corresponding config in XML template.

For example, if you don't have juniper-junos NED available, then comment juniper configuration by placing XML comment in template as below:

```xml
<!-- <configuration xmlns="http://xml.juniper.net/xnm/1.1/xnm">
    .....
    .....
</configuration> -->
```


# Demo Link

[Link to NSO DevNet demo recording](https://community.cisco.com/t5/nso-developer-hub-videos/how-to-automate-port-turnup-with-nso/ba-p/3668012)


# Contact Email:

For any queries & feedback, please contact the following mailer alias: as-nso-service-packs@cisco.com
