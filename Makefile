build:
	python setup.py build

install:
	python setup.py install;
	cd dependencies/python-louvain-0.3;
	python setup.py install;

test:
	cd test; python test.py
