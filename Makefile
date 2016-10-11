install:
	python setup.py install;

test_hermes:
	if [ ! -d "test/data" ]; then mkdir test/data; fi
	python test/test.py test
	hermes -e test/data/random-edge-list.csv -n test/data/random-node-list.csv
