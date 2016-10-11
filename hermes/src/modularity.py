import community
import networkx as nx

from utils import _add_to_graph

def louvainModularity(G, preserved=True):
  partition = community.best_partition(G)
  if preserved:
    _add_to_graph(G, partition, 'louvain_community')
