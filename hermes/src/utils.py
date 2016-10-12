import networkx as nx

def _get_section_config(setting, name):
   return lambda x: setting.get(name, x)

def _add_to_graph(G, new_attrs, attr_name):
  for node, val in new_attrs.iteritems():
    G.node[node][attr_name] = val
