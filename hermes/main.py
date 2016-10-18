import sys, getopt
import ConfigParser
import os.path as op

import hermes
import hermes.src.construct as construct
import hermes.src.centrality as centrality
import hermes.src.modularity as modularity
from hermes.src.utils import _get_section_config

def _getConfig():
	packagedir = hermes.__path__[0]
	config = ConfigParser.ConfigParser()
	config.read(op.join(packagedir,'config.cfg'))
	return config

def _formatUsage(setting):
	return '''Usage:
	hermes [convert] [-n <node-list-file-name>] [-e <edge-list-file-name>] [-d] [-o <output-file-name>] [<command>] [<command>] [<command>] ...

	-n, --node-list\tinput node list file name (CSV)
	-e, --edge-list\tinput edge list file name (CSV)
	-d, --directed\tconstuct directed graph
	-o, --ofile\toutput file name (CSV or GEXF) (default = %s-node.csv)

	convert\t\tconvert CSV files to GEXF file (default input files = %s %s, output file = %s.gexf)

default node list: %s; and edge-list: %s

Commands:
	degree-centrality\tcompute degree centrality (default to in-degree if the graph is directed)
	in-degree-centrality\tcompute in-degree centrality (only works with directed graph)
	out-degree-centrality\tcompute out-degree centrality (only works with directed graph)
	closeness-centrality\tcompute closeness centrality
	betweenness-centrality\tcompute betweenness centrality
	eigenvector-centrality\tcompute eigenvector centrality
	centrality\t\tcompute all centrality values (depending on whether the graph is directed or not)
	modularity\t\tpreform community detection

default command(s) = %s

Use -h or --help to show usage information.
	''' % (
		setting.get('Default', 'output-file'),
		setting.get('Default', 'node-list'),
		setting.get('Default', 'edge-list'),
		setting.get('Default', 'convert-node-list'),
		setting.get('Default', 'convert-edge-list'),
		setting.get('Default', 'output-file'),
		', '.join(setting.get('Default', 'analysis').split(','))
	)

def _getMethodName(name):
	return 'get'+ ''.join(map(lambda x: x.capitalize(), name.split('-')))


def _formatErrorAndExit(message):
	print 'ERROR: %s' % (message)
	print '(Use -h or --help to show usage information.)'
	sys.exit(2)

def _validateFile(file_name):
	if op.isfile(file_name):
		return True
	else:
		_formatErrorAndExit('File %s not found.' % (file_name))

def _getInputFiles(opts, setting, prefix = ''):
	directed = False
	node_list = None
	edge_list = None
	output_file = setting.get('Default', 'output-file')

	for opt, arg in opts:
		if opt in ('-d', '--directed'):
			directed = True
		elif opt in ('-n', '--node-list'):
			_validateFile(arg)
			node_list = arg
		elif opt in ('-e', '--edge-list'):
			_validateFile(arg)
			edge_list = arg
		elif opt in ('-o', '--ofile'):
			output_file = arg

	if not node_list and not edge_list:
		node_list = setting.get('Default', prefix+'node-list')
		edge_list = setting.get('Default', prefix+'edge-list')

	# print 'Opening files %s %s' % (edge_list, node_list)
	return (directed, node_list, edge_list, output_file)

def _getGraph(edge_list, node_list, directed, constructor_setting):
	if edge_list or node_list:
		print 'Constructing graph'
		return construct.buildGraph(edge_list, node_list, constructor_setting, directed)
	else:
		_formatErrorAndExit('No input file, edge list or node list.')

def convert(argv, setting):
	try:
		opts, args = getopt.getopt(argv[2:],'n:e:o:d',['node-list=','edge-list=','ofile=', 'directed'])
	except getopt.GetoptError:
		_formatErrorAndExit('Invalid input options or arguments.')

	directed, node_list, edge_list, output_file = _getInputFiles(opts, setting, 'convert-')

	constructor_setting = _get_section_config(setting, 'Constructor')
	G = _getGraph(edge_list, node_list, directed, constructor_setting)

	file_name = construct.dumpToGephi(G, output_file)
	print 'Outputting to GEXF %s' % (file_name)

def main(argv, setting):
	try:
		opts, args = getopt.getopt(argv[1:],'n:e:o:hd',['node-list=','edge-list=','ofile=','help', 'directed'])
	except getopt.GetoptError:
		_formatErrorAndExit('Invalid input options or arguments.')

	# print opts
	# print args

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print _formatUsage(setting)
			sys.exit(2)

	directed, node_list, edge_list, output_file = _getInputFiles(opts, setting)

	constructor_setting = _get_section_config(setting, 'Constructor')
	G = _getGraph(edge_list, node_list, directed, constructor_setting)

	if not args:
		args = setting.get('Default','analysis').split(',')
	else:
		# remove redundent args
		args = list(set(args))

	for command in args:
		print 'Processing analysis: %s' % (command)
		if command == 'modularity':
			modularity.louvainModularity(G)
		elif command == 'centrality':
			centrality.getCentrality(G, setting)
		else:
			func_name = _getMethodName(command)
			if func_name in centrality.__dict__:
				if setting.has_section(func_name):
					centrality.__dict__[func_name](G, _get_section_config(setting, func_name))
				else:
					centrality.__dict__[func_name](G)
			else:
				_formatErrorAndExit('Invalid command %s.' % (command))

	if output_file:
		file_names = construct.dumpToCsv(G, output_file, constructor_setting)
		print 'Outputting to CSV %s' % (file_names)

if __name__ == "__main__":
	setting = _getConfig()
	argv = sys.argv

	if len(argv) > 1 and argv[1] == 'convert':
		convert(argv, setting)
	else:
		main(argv, setting)

