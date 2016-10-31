import networkx as nx

from dependencies.edgeswap import EdgeSwapGraph
from utils.utils import _add_to_graph, _progress_bar	

def growBySwapEdges(G, func=None):
	swappableG = EdgeSwapGraph()

	for n1, n2, data in G.edges_iter(data=True):
		if not func or func(data):
			swappableG.add_edge(n1, n2)

	return swappableG

def growthStatistics(swappableG, n, statistics):
	print '# nodes: %d' % (swappableG.number_of_nodes())
	print '# edges: %d' % (swappableG.number_of_edges()) 

	n = swappableG.number_of_nodes() * n
	p_vals = {}
	for s in statistics:
		sum_ = 0
		sum_sq = 0

		for i in range(n):
			_progress_bar(i*100.0/(n-1), True)
			rand_graph = swappableG.randomize_by_edge_swaps(5)
			obs = nx.__dict__[s](rand_graph)
			if type(obs) == type({}):
				obs = sum(obs.values())
			sum_ += obs
			sum_sq += obs * obs
		print ' done '+s
		mean = sum_ * 1.0 / n
		var = (sum_sq - sum_ * sum_ * 0.1 / n) / (n - 1)
		sample = nx.__dict__[s](swappableG)
		if type(sample) == type({}):
			sample = sum(sample.values())

		p_vals[s] = {
			'p': (sample - mean) / var,
			'mean': mean,
			'sample': sample,
			'var': var
		}

	return p_vals