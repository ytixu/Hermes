import csv
import networkx as nx


def _buildFromNodeList(file_name, setting, G):
	print setting
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=setting('delimiter') if setting('delimiter') != 'tab' else '\t',
											quotechar=setting('quotechar'))
		attr_indices = {}
		id_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lambda x: x.lower(), row)
				intersect_keys = list(set(setting('node_attributes')).intersection(lowered_keys))
				attr_indices = {lowered_keys.index(x): x for x in intersect_keys}
				id_index = lowered_keys.index(setting('id'))

				# if id_index < 0:
					# throw exception
				continue

			G.add_node(row[id_index])
			for index, attr in attr_indices.iteritems():
				G.node[row[id_index]][attr] = row[index]

	return G


def _buildFromEdgeList(file_name, setting, G):
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=setting('delimiter') if setting('delimiter') != 'tab' else '\t',
											quotechar=setting('quotechar'))
		attr_indices = {}
		source_index = -1
		target_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lambda x: x.lower(), row)
				intersect_keys = list(set(setting('edge_attributes')).intersection(lowered_keys))
				attr_indices = {lowered_keys.index(x): x for x in intersect_keys}
				source_index = lowered_keys.index(setting('source'))
				source_index = lowered_keys.index(setting('target'))

				# if source_index < 0:
				# 	# throw exception
				# if target_index < 0:
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
		G = _buildFromEdgeList(edge_list, setting, G)

	if node_list:
		G = _buildFromNodeList(node_list, setting, G)

	return G


def buildDirectedGraph(edge_list, node_list, setting):
	return buildGraph(edge_list, node_list, setting, True)


def _formatFileName(file_name, ext):
	try:
		file_name.index('.' + ext)
	except ValueError:
		return file_name+'.'+ext

def dumpGraph(G, file_name):
	nx.write_gpickle(G, _formatFileName(file_name, 'gpickle'))

def loadGraph(file_name):
	return nx.read_gpickle(file_name)

def dumpToGephi(G, file_name):
	nx.write_gexf(G, _formatFileName(file_name, 'gexf'))

def loadFromGephi(file_name):
	return nx.read_gexf(file_name)
