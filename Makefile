build:
	python setup.py build

install:
	python setup.py install;
	# cd dependencies/python-louvain-0.3;
	python dependencies/python-louvain-0.3/setup.py install;

test:
	cd test; python test/test.py
