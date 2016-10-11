import csv
import random
import netoworkx as nx

G = nx.powerlaw_cluster_graph(111, 5, 0.11)

with open('data/random-node-list.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['id','label','weigth'])
	for node in G.nodes():
		spamwriter.writerow([node, ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)), random.randint(1, 11)])

with open('data/random-edge-list.csv', 'wb') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter='\t', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['source','target','label','weigth'])
	for u, v in G.edges():
		spamwriter.writerow([u, v, random.randint(999, 9999), random.randint(11, 111)])

