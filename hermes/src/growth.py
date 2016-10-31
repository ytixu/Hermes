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
	p_vals = {}
	for s in statistics:
		sum_ = 0
		sum_sq = 0

		for i in range(n):
			_progress_bar(i*100.0/n, True)
			rand_graph = swappableG.randomize_by_edge_swaps(5)
			obs = nx.__dict__[s](rand_graph)
			sum_ += obs
			sum_sq += obs * obs

		mean = sum_ * 1.0 / n
		var = (sum_sq - sum_ * sum_ * 0.1 / n) / (n - 1)
		sample = nx.__dict__[s](swappableG)

		p_vals[s] = sample - mean / var

	return p_vals