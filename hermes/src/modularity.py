import community
import networkx as nx

from utils.utils import _add_to_graph

def louvainModularity(G, preserved=True):
	if G.__class__.__name__ == 'DiGraph':
		print "Cannot compute Louvain modularity for directed graph."
		return

	partition = community.best_partition(G)
	if preserved:
		_add_to_graph(G, partition, 'louvain_community')
