import math
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
	sum_ = {s: 0 for s in statistics}
	sum_sq = {s: 0 for s in statistics}

	for i in range(n):
		_progress_bar(i*100.0/(n-1), True)
		rand_graph = swappableG.randomize_by_edge_swaps(5)

		for s in statistics:
			obs = nx.__dict__[s](rand_graph)

			if type(obs) == type({}):
				obs = sum(obs.values())
			sum_[s] += obs
			sum_sq[s] += obs * obs

	for s in statistics:
		mean = sum_[s] * 1.0 / n
		std = math.sqrt((sum_sq[s] - sum_[s] * mean) / (n - 1))
		sample = nx.__dict__[s](swappableG)
		if type(sample) == type({}):
			sample = sum(sample.values())

		p_vals[s] = {
			'p': (sample - mean) / std,
			'mean': mean,
			'sample': sample,
			'std': std
		}

	return p_vals