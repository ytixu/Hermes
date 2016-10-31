import community
import networkx as nx

from utils.utils import _add_to_graph, _progress_bar

def louvainModularity(G, preserved=True):
	if G.__class__.__name__ == 'DiGraph':
		print "Cannot compute Louvain modularity for directed graph."
		return

	partition = community.best_partition(G)
	if preserved:
		_add_to_graph(G, partition, 'louvain_community')
	else:
		return partition

def connectedComponents(G, preserved=True):
	components = nx.connected_components(G)
	
	if preserved:
		_add_to_graph(G, components, 'connected_components')
	else:
		return components

def louvainModularityByComponent(G, setting, preserved=True):
	components = nx.connected_components(G)
	directed = True if G.__class__.__name__ == 'DiGraph' else False
	t = float(setting('t'))
	n = G.number_of_nodes()
	count = 0

	for i, nodes in enumerate(components):
		_progress_bar(i)

		if len(nodes) * 1.0 / n < t:
			if preserved:
				_add_to_graph(G, {node: count for node in nodes}, 'louvain_community')
			count += 1
			continue

		subG = G.subgraph(nodes)
		partition = community.best_partition(G)
		if preserved:
			_add_to_graph(G, {node: count+comm for node, comm in partition.iteritems()}, 'louvain_community')

		count += len(partition) 
	print 'done'
