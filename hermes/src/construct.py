import csv
import networkx as nx


def _getDelimiter(setting):
	return setting('delimiter') if setting('delimiter') != 'tab' else '\t',

def _buildFromNodeList(file_name, setting, G):
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=_getDelimiter(setting)
											quotechar=setting('quotechar'))
		attr_indices = {}
		id_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lambda x: x.lower(), row)
				intersect_keys = list(set(setting('node_attributes').split(',')).intersection(lowered_keys))
				attr_indices = {lowered_keys.index(x): x for x in intersect_keys}
				id_index = lowered_keys.index(setting('id'))

				if id_index < 0:
					raise Exception('No column "%s" found in file %s.' % (setting('id'), file_name))
				continue

			G.add_node(row[id_index])
			for index, attr in attr_indices.iteritems():
				if attr in setting('float_column'):
					G.node[row[id_index]][attr] = float(row[index])
				else:
					G.node[row[id_index]][attr] = row[index]

	return G


def _buildFromEdgeList(file_name, setting, G):
	with open(file_name, 'r') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=_getDelimiter(setting)
											quotechar=setting('quotechar'))
		attr_indices = {}
		source_index = -1
		target_index = -1
		for i, row in enumerate(spamreader):
			if i == 0:
				lowered_keys = map(lambda x: x.lower(), row)
				intersect_keys = list(set(setting('edge_attributes').split(',')).intersection(lowered_keys))
				attr_indices = {lowered_keys.index(x): x for x in intersect_keys}
				source_index = lowered_keys.index(setting('source'))
				target_index = lowered_keys.index(setting('target'))

				if source_index < 0:
					raise Exception('No column "%s" found in file %s.' % (setting('source'), file_name))
				if target_index < 0:
					raise Exception('No column "%s" found in file %s.' % (setting('target'), file_name))

				continue

			G.add_edge(row[source_index], row[target_index])
			for index, attr in attr_indices.iteritems():
				if attr in setting('float_column'):
					G[row[source_index]][row[target_index]][attr] = float(row[index])
				else:
					G[row[source_index]][row[target_index]][attr] = row[index]

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


def _formatFileName(file_name, ext, delimiter = '.'):
	try:
		file_name.index(delimiter + ext)
	except ValueError:
		return file_name+delimiter+ext

def _dumpCsv(G, file_name, header, generator):
	with open(_formatFileName(file_name, 'csv'), 'w') as csv_file:
		spamreader = csv.reader(csv_file, delimiter=_getDelimiter(setting)
											quotechar=setting('quotechar')):
		spamwriter.writerow(header)
		for row in generator:
			spamwriter.writerow(row)

def _nodeGen(G):
	for node, data in G.nodes_iter(data=True):
		yield [node] + data.values()

def _nodeGen(G):
	for nodes, data in G.edge_iter(data=True):
		yield list(nodes) + data.values()

def dumpCsv(G, file_name):
	# Dump node list
	header = ['ID'] + G.nodes(data=True)[0][1].keys()
	_dumpCsv(G, _formatFileName(file_name, 'node', '-'), header, _nodeGen(G))

	# Dump node edges
	header = ['SOURCE', 'TARGET'] + G.edges(data=True)[0][1].keys()
	_dumpCsv(G, _formatFileName(file_name, 'edge', '-'), header, _edgeGen(G))

def dumpToGephi(G, file_name):
	nx.write_gexf(G, _formatFileName(file_name, 'gexf'))

def loadFromGephi(file_name):
	return nx.read_gexf(file_name)
