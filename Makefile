install:
	python setup.py install;

test:
	mkdir test/data;
	python test/test.py;
