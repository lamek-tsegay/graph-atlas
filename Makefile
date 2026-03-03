.PHONY: install test demo clean

install:
	python3 -m venv .venv && . .venv/bin/activate && pip install -e . && pip install pytest

test:
	. .venv/bin/activate && pytest -q

demo:
	PYTHONPATH=src python3 examples/demo_network.py

clean:
	rm -rf .venv __pycache__ .pytest_cache