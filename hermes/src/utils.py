import networkx as nx

def _add_to_graph(G, new_attrs, attr_name):
  for node, val in new_attrs:
    G.node[node][attr_name] = val
