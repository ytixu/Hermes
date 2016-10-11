import sys, getopt
import ConfigParser
import os.path as op

import hermes
import hermes.src.construct as construct
import hermes.src.centrality as centrality
import hermes.src.modularity as modularity

def _getConfig():
   packagedir = hermes.__path__[0]
   config = ConfigParser.ConfigParser()
   config.read(op.join(packagedir,'config.cfg'))
   return config

def _formatUsage(name):
   return '''Usage:
   %s -n <node-list-file> -e <edge-list-file> -d -g -i <input-graph-object-file> -g -o <output-file> <command> <command> <command> ...

   -n, --node-list\tinput node list file name (csv)
   -e, --edge-list\tinput edge list file name (csv)
   -d, --deirected\tconstuct directed graph
   -i, --ifile\t\tinput object file name (for pickle or Gephi format)
   -o, --ofile\t\toutput file name (for pickle or Gephi format) (default = out.gefx)
   -g, --gephi\t\tinput/output in Gephi format

Commands:
   degree-centrality\t\tcompute degree centrality (default in-degree if graph is directed)
   in-degree-centrality\t\tcompute in-degree centrality
   out-degree-centrality\tcompute out-degree centrality
   closseness-centrality\tcompute closseness centrality
   betweenness-centrality\tcompute betweenness centrality
   eigenvector-centrality\tcompute eigenvector centrality
   centrality\t\t\tcompute all centrality values (depending on whether the graph is directed or not)
   modularity\t\t\tpreform community detection

If no command is inputted, default behanvior will compute all of the above.

Use -h or --help to show usage information.
   ''' % (name)

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


def main(argv):
   try:
      opts, args = getopt.getopt(argv[1:],'n:e:i:o:gphd',['node-list=','edge-list=','ifile=','ofile=','gephi','help', 'directed'])
   except getopt.GetoptError:
      _formatErrorAndExit('Invalid input options or arguments.')

   # print opts
   # print args

   gephi = False
   directed = False
   node_list = None
   edge_list = None
   input_file = None
   output_file = ('out', True)

   for opt, arg in opts:
      if opt in ('-h', '--help'):
         print _formatUsage(argv[0])
         sys.exit(2)
      if opt in ('-g', '--gephi'):
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
         _validateFile(arg)
         output_file = (arg, gephi)
         gephi = False

   G = None
   setting = _getConfig()
   print setting.items('Constructor')

   if input_file:
      print 'Loading graph %s' % input_file[0]
      if input_file[1]:
         G = construct.loadFromGephi(input_file[0])
      else:
         G = construct.loadGraph(input_file[0])
   elif edge_list or node_list:
      print 'Constructing graph'
      G = construct.buildGraph(edge_list, node_list, setting.items('Constructor'), directed)
   else:
      _formatErrorAndExit('No input file, edge list or node list.')


   if args:
      for command in args:
         print 'Processing command: %s' % (command)
         if command == 'modularity':
            modularity.louvainModularity(G)
         else:
            func_name = _getMethodName(command)
            if func_name in centrality.__dict__:
               if setting.has_section(func_name):
                  centrality.__dict__[func_name](G, setting.items(func_name))
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
   main(sys.argv)

