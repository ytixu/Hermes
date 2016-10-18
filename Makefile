install:
	python setup.py install;

test_hermes:
	if [ ! -d "test/data" ]; then mkdir test/data; fi
	python test/test.py test;
	hermes -e test/data/random-edge-list.csv -n test/data/random-node-list.csv -o out;
	hermes convert -e test/data/random-edge-list.csv -n out.csv -o out;

more_tests:
	if [ ! -d "test/data" ]; then mkdir test/data; fi
	python test/test.py test;
	hermes -e test/data/random-edge-list.csv -d -o out-edge in-degree-centrality out-degree-centrality degree-centrality closeness-centrality betweenness-centrality eigenvector-centrality modularity;
	hermes -n test/data/random-node-list.csv -o out-node degree-centrality closeness-centrality betweenness-centrality eigenvector-centrality modularity;
	hermes convert -e test/data/random-edge-list.csv -n out-edge.csv -d -o out-edge-d
	hermes convert -e test/data/random-edge-list.csv -n out-edge.csv -o out-edge
	hermes convert -n out-node.csv -o out-node

