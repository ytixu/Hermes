import sys
import networkx as nx

def _get_section_config(setting, name):
   return lambda x: setting.get(name, x) if (',' not in setting.get(name, x) or len(setting.get(name, x)) < 3) else setting.get(name, x).split(',')

def _add_to_graph(G, new_attrs, attr_name):
 	for node, val in new_attrs.iteritems():
		G.node[node][attr_name] = val

###
# Helper for CSV file delimiter from config file
#
def _getDelimiter(setting):
	return setting('delimiter') if setting('delimiter') != 'tab' else '\t'


###
# UI
#
def _progress_bar(update, percent=False):
	sys.stdout.write('\r')
	if percent:
		sys.stdout.write("[%.0f]" % (update))
	else:
		sys.stdout.write("[%d]" % (update))
	sys.stdout.flush()
