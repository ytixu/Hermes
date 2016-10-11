import networkx as nx

from utils import _add_to_graph

def getDegreeCentrality(G, in_degree=True, preserved=True):
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

def getClosessnessCentrality(G, u=None, distance=None, normalized=True, preserved=True):
  cl = nx.closeness_centrality(G, u, distance, normalized)
  if preserved:
    _add_to_graph(G, cl, 'closeness_centrality')

def getBetweennessCentrality(G, k=None, normalized=True, weight=None, endpoints=False, seed=None, preserved=True):
  bt = nx.betweenness_centrality(G, k, normalized, weight, endpoints, seed)
  if preserved:
    _add_to_graph(G, bt, 'betweenness_centrality')

def getEigenvectorCentrality(G, max_iter=100, tol=1e-06, nstart=None, weight='weight', preserved=True):
  eg = nx.eigenvector_centrality(G, max_iter, tol, nstart, weight)
  if preserved:
    _add_to_graph(G, eg, 'eigenvector_centrality')
