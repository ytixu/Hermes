import csv
import networkx as nx

from hermes.utils.utils import _getDelimiter

def _percent_diff(a, b):
	return 2*abs(a-b)/(a+b)

def _not_null(val):
	if not val or val == 'NA' or val == '0.00' or val == '0':
		return False
	return True

def _is_not_price(key, setting):
	if key in setting('price_columns') or key in setting('msrp_columns') or key in setting('cost_columns'):
		return False

	return True

def _compute_score(a, b, attr, setting):
	score = 0
	for key in setting('must_match'):
		if key in attr[a] and (attr[a][key] != attr[b][key]):
			return 0

	# non-float values
	for key, val in attr[a].iteritems():
		if key in attr[b]:
			if _is_not_price(key):
				if attr[b][key] == val:
					score += 1
	# price values
	for price_name in ['price_columns', 'msrp_columns', 'cost_columns']:
		max_sim = max([_percent_diff(float(attr[a][key]), float(attr[b][key])) 
								for key in setting(price_name) if key in attr[a]])

		if max_sim < setting('max_diff'):
			score += 1

	return score

def getGraph(file_name, setting):
	G = nx.Graph()
	properties = {}
	node_attr = {}

	with open(file_name, 'r') as csv_file:
		reader = csv.reader(csv_file, delimiter=_getDelimiter(setting), quotechar=setting('quotechar'))
		keys = []
		for i, row in enumerate(reader):
			if i == 0:
				keys = row[1:]
				continue
			prod = i
			node_attr[prod] = {}
			G.add_node(prod)
			sim = []
			for j, val in enumerate(row):
				key = keys[j]
				if _not_null(val):
					if _is_not_price(key):
						prop_key = key+'-'+val
						if key in setting('must_match'):
							if prop_key not in properties:
								properties[prop_key] = []
							else:
								sim = set(list(sim) + properties[prop_key])
							properties[prop_key].append(prod)

					node_attr[prod][key] = val
				else:
					node_attr[prod][key] = 0

			for sim_node in sim:
				w = _compute_score(sim_node, prod, node_attr)
				if w == 0:
					continue
				G.add_edge(sim_node, prod, weight=w)

			# if i > 40:
			# 	break

	return G