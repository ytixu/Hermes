import networkx as nx

from utils import _add_to_graph, _get_section_config

def getDegreeCentrality(G, preserved=True, in_degree=True):
	dc = {}
	name = ''
	if G.__class__.__name__ == 'DiGraph':
		if in_degree:
			dc = nx.in_degree_centrality(G)
			name = 'in_degree_centrality'
		else:
			dc = nx.out_degree_centrality(G)
			name = 'out_degree_centrality'
	else:
		dc = nx.degree_centrality(G)
		name = 'degree_centrality'

	if preserved:
		_add_to_graph(G, dc, name)

def getInDegreeCentrality(G, preserved=True):
	return getDegreeCentrality(G, preserved)

def getOutDegreeCentrality(G, preserved=True):
	return getDegreeCentrality(G, preserved, False)

def getClosenessCentrality(G, setting, preserved=True):
	u = setting('u') if setting('u') else None
	distance = setting('distance') if setting('distance') else None
	normalized = setting('normalized')
	cl = nx.closeness_centrality(G, u, distance, normalized)
	if preserved:
		_add_to_graph(G, cl, 'closeness_centrality')

def getBetweennessCentrality(G, setting, preserved=True):
	k = setting('k') if setting('k') else None
	normalized = setting('normalized')
	weight = setting('weight') if setting('weight') else None
	endpoints = setting('endpoints')
	seed = setting('seed') if setting('seed') else None
	bt = nx.betweenness_centrality(G, k, normalized, weight, endpoints, seed)
	if preserved:
		_add_to_graph(G, bt, 'betweenness_centrality')

def getEigenvectorCentrality(G, setting, preserved=True):
	max_iter = int(setting('max_iter'))
	tol = float(setting('tol'))
	nstart = setting('nstart') if setting('nstart') else None
	weight = setting('weight')
	eg = nx.eigenvector_centrality(G, max_iter, tol, nstart, weight)
	if preserved:
		_add_to_graph(G, eg, 'eigenvector_centrality')


###
# Compute all the centrality measures
#
def getCentrality(G, setting, preserved=True):
	if G.__class__.__name__ == 'DiGraph':
		getInDegreeCentrality(G, preserved)
		getOutDegreeCentrality(G, preserved)
	else:
		getDegreeCentrality(G, preserved)

	getClosenessCentrality(G, _get_section_config(setting, 'getClosenessCentrality'), preserved)
	getBetweennessCentrality(G, _get_section_config(setting, 'getBetweennessCentrality'), preserved)
	getEigenvectorCentrality(G, _get_section_config(setting, 'getEigenvectorCentrality'), preserved)