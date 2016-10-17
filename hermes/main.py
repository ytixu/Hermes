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
	hermes [<command>] [-n <node-list-file-name>] [-e <edge-list-file-name>] [-d] [-o <output-file-name>]

	-n, --node-list\tinput node list file name (CSV) (default = %s)
	-e, --edge-list\tinput edge list file name (CSV) (default = %s)
	-d, --directed\tconstuct directed graph
	-o, --ofile\t\toutput file name (CSV) (default = out)

Commands:
	convert\t\t\tconvert CSV files to GEXF file (default output file = out)
	degree-centrality\t\tcompute degree centrality (default to in-degree if the graph is directed)
	in-degree-centrality\t\tcompute in-degree centrality (only works with directed graph)
	out-degree-centrality\tcompute out-degree centrality (only works with directed graph)
	closeness-centrality\tcompute closeness centrality
	betweenness-centrality\tcompute betweenness centrality
	eigenvector-centrality\tcompute eigenvector centrality
	centrality\t\t\tcompute all centrality values (depending on whether the graph is directed or not)
	modularity\t\t\tpreform community detection

default command = %s

Use -h or --help to show usage information.
	''' % (
		setting.get('Default', 'node-list'),
		setting.get('Default', 'edge-list'),
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

def main(argv, setting):
	try:
		opts, args = getopt.getopt(argv[1:],'n:e:i:o:gphd',['node-list=','edge-list=','ifile=','ofile=','gexf','help', 'directed'])
	except getopt.GetoptError:
		_formatErrorAndExit('Invalid input options or arguments.')

	# print opts
	# print args

	gephi = False
	directed = False
	node_list = setting.get('Default', 'node-list')
	edge_list = setting.get('Default', 'edge-list')
	input_file = None
	output_file = ('out', True)

	for opt, arg in opts:
		if opt in ('-h', '--help'):
			print _formatUsage(setting)
			sys.exit(2)
		if opt in ('-g', '--gexf'):
			gephi = True
		elif opt in ('-d', '--directed'):
			directed = True
		elif opt in ('-n', '--node-list'):
			_validateFile(arg)
			node_list = arg
		elif opt in ('-e', '--edge-list'):
			_validateFile(arg)
			edge_list = arg
		elif opt in ('-i', '--ifile'):
			_validateFile(arg)
			input_file = (arg, gephi)
			gephi = False
		elif opt in ('-o', '--ofile'):
			output_file = (arg, gephi)
			gephi = False

	G = None

	if input_file:
		print 'Loading graph %s' % input_file[0]
		if input_file[1]:
			G = construct.loadFromGephi(input_file[0])
		else:
			G = construct.loadGraph(input_file[0])
	elif edge_list or node_list:
		print 'Constructing graph'
		G = construct.buildGraph(edge_list, node_list, _get_section_config(setting, 'Constructor'), directed)
	else:
		_formatErrorAndExit('No input file, edge list or node list.')


	if not args:
		args = setting.get('Default','analysis').split(',')

	for command in args:
		if command == 'no-analysis':
			break
		print 'Processing command: %s' % (command)
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
		print 'Outputting to %s' % (output_file[0])
		if output_file[1]:
			construct.dumpToGephi(G, output_file[0])
		else:
			construct.dumpGraph(G, output_file[0])


if __name__ == "__main__":
	setting = _getConfig()
	argv = sys.argv
	if not len(sys.argv) > 1:
		argv = sys.argv + setting.get('Default', 'argv').split(' ')

	if argv[1] == 'convert':
		argv.remove('convert')
		argv.append('no-analysis')

	main(argv, setting)

