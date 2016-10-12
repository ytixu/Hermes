import csv
import random
import string
import sys

import networkx as nx

file_path = (sys.argv[1] if len(sys.argv) > 1 else '.') + '/data/'

G = nx.gaussian_random_partition_graph(111, 55, .11, .033, .033)

with open(file_path+'random-node-list.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
	spamwriter.writerow(['id','label','weight'])
	for node in G.nodes():
		spamwriter.writerow([node, ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)), random.randint(1, 11)])

with open(file_path+'random-edge-list.csv', 'w') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"')
	spamwriter.writerow(['source','target','label','weight'])
	for u, v in G.edges():
		spamwriter.writerow([u, v, random.randint(999, 9999), random.randint(11, 111)])

