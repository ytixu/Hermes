import csv
import pickle
import networkx as nx


###
# Build graph from node list.
#
#
def buildFromNodeList(file_name, setting, G):
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(file_name, delimiter=setting.delimiter,
											quotechar=setting.quotechar)
		attr_indices = {}
		id_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lower, row)
				attr_indices = {index(x, lowered_keys): x for x in intersect(setting.node_attributes, lowered_keys)}
				id_index = index(setting.id, lowered_keys)

				if id_index < 0:
					# throw exception
				continue

			G.add_node(row[id_index])
			for index, attr in attr_indices.iteritems():
				G.node[row[id_index]][attr] = row[index]

	return G


def buildFromEdgeList(file_name, setting, G):
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(file_name, delimiter=setting.delimiter,
											quotechar=setting.quotechar)
		attr_indices = {}
		source_index = -1
		target_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lower, row)
				attr_indices = {index(x, lowered_keys): x for x in intersect(setting.edge_attributes, lowered_keys)}
				source_index = index(setting.source, lowered_keys)
				source_index = index(setting.target, lowered_keys)

				if source_index < 0:
					# throw exception
				if target_index < 0:
					# throw exception
				continue

			G.add_edge(row[source_index], row[target_index])
			for index, attr in attr_indices.iteritems():
				G[source_index][target_index][attr] = row[index]

	return G

def buildGraph(edge_list, node_list, setting, directed=False):
	G = None
	if directed:
		G = nx.DiGraph()
	else:
		G = nx.Graph()

	if edge_list:
		G = buildFromNodeList(edge_list, setting, G)

	if node_list:
		G = buildFromNodeList(node_list, setting, G)

	return G


def buildDirectedGraph(edge_list, node_list, setting):
	return buildGraph(edge_list, node_list, setting, True)