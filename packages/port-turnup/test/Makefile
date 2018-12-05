DIRS = external internal

ifeq ($(BUILD_JOB),external)
DIR = external
endif

ifeq ($(BUILD_JOB),internal_realhw)
DIR = internal
JOB_DIR = realhw
endif

ifeq ($(BUILD_JOB),internal_simulated)
DIR = internal
JOB_DIR = simulated
endif

ifeq ($(BUILD_JOB),)
DIR = internal
JOB_DIR = simulated
endif

all: clean-netsim create-netsim start-netsim load-device sync-device test

create-netsim: 
	    ncs-netsim create-network ../../cisco-ios 2 ios_; \
	    ncs-netsim add-to-network ../../cisco-nx 3 nx_; \
	    ncs-netsim add-to-network ../../juniper-junos 3 junos_; \
	    ncs-netsim add-to-network ../../arista-dcs 3 arista_; \
	    ncs-netsim add-to-network ../../cisco-iosxr 2 xr_; \
	    ncs-netsim ncs-xml-init > devices.xml

start-netsim:
	 ncs-netsim start 

load-device:
	ncs_load -l -m -F x -u admin -g admin devices.xml

sync-device:
	echo "request devices fetch-ssh-host-keys" | ncs_cli -u admin
	echo "request devices sync-from" | ncs_cli -u admin

stop-netsim:
	ncs-netsim stop 

clean:
	$(MAKE) -C $(DIR) clean JOB_DIR=$(JOB_DIR) || exit

clean-netsim:
	if [ -d netsim ]; then         \
		ncs-netsim stop;           \
		ncs-netsim delete-network; \
		rm -rf devices.xml; \
	fi
	
test:
	$(MAKE) -C $(DIR) test JOB_DIR=$(JOB_DIR) || exit 1

desc:
	@echo "==Test Cases for NED=="
	@for d in $(DIRS) ; do \
	  $(MAKE) -sC $$d desc || exit 1; \
	done
