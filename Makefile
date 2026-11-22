PYTHON ?= python

PROJECTS := \
	projects/energy-economics/merit-order-dispatch \
	projects/energy-economics/storage-arbitrage \
	projects/energy-economics/non-exporting-btm-storage \
	projects/power-systems/two-node-congestion \
	projects/power-systems/three-bus-dc-power-flow \
	projects/power-systems/radial-der-hosting-capacity \
	projects/power-systems/flexible-interconnection \
	projects/power-systems/frequency-response-dynamics \
	projects/power-systems/stochastic-adequacy \
	projects/power-systems/network-flow-resilience \
	projects/econometrics/ols-energy-demand

.PHONY: test docs clean

test:
	@set -e; for project in $(PROJECTS); do \
		echo "=== Testing $$project ==="; \
		(cd $$project && $(PYTHON) -m pip install -q -r requirements.txt && $(PYTHON) -m unittest discover -s . -p 'test_*.py' -v); \
	done

docs:
	$(PYTHON) scripts/prepare_docs.py
	mkdocs build --strict

clean:
	rm -rf site site_docs
