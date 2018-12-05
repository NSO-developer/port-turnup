PORTTURNUP = pt_01_with_all_params.lux \
          pt_02_with_all_params.lux

LUX_FILES = $(PORTTURNUP)

LOG_PATH = $(shell date +%Y-%m-%dT%H:%M:%S%z)

# export all variables so child Make invocations can access
export

test:
	$(MAKE) -C tests/ test

test-portturnup:
	$(MAKE) -C tests/ test-portturnup

clean-logs:
	rm -rf lux_logs/*


LUX_REPORTS = $(LUX_FILES:%=../test-reports/%.xml)

copy-lux-logs: $(LUX_REPORTS)
$(LUX_REPORTS): ../test-reports/%.xml: lux_logs/%/lux_summary.log
	mkdir -p $(@D)
	python lux-to-junit.py $< > $@

clean:
	rm -rf lux_logs
	rm -f *.ec
	rm -f *.xml

clean-default: clean
	cd ../run && \
	ncs --stop; \
	ncs-netsim stop; \
	$(shell cd ../run && find . -type f -name "*.cdb" -exec rm {} \;) \
	rm -rf state; mkdir state; \
	ncs; \
	ncs-netsim start;
