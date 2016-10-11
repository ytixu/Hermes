build:
	python setup.py build

install:
	python setup.py install;

test:
	cd test; python test/test.py
