init:
	pip install -r requirements.txt -r requirements-test.txt

test:
	pytest -vs tests/
