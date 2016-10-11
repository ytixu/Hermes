import sys, getopt
import ConfigParser

import src.construct as construct
import src.centrality as centrality
import src.modularity as modularity

def getConfig():
   config = ConfigParser.ConfigParser()
   config.read('../config.cfg')
   return config

def formatUsage(name):
   return '''Usage:
   %s -n <node-list-file> -e <edge-list-file> -d -g -i <input-graph-object-file> -g -o <output-file> <command> <command> <command> ...

   -n, --node-list\tinput node list file name (csv)
   -e, --edge-list\tinput edge list file name (csv)
   -d, --deirected\tconstuct directed graph
   -i, --ifile\t\tinput object file name (for pickle or Gephi format)
   -o, --ofile\t\toutput file name (for pickle or Gephi format) (default = out.gefx)
   -g, --gephi\t\tinput/output in Gephi format

Commands:
   degree-centrality\t\tcompute degree centrality
   in-degree-centrality\t\tcompute in degree centrality
   out-degree-centrality\tcompute out degree centrality
   closseness-centrality\tcompute closseness centrality
   betweenness-centrality\tcompute betweenness centrality
   eigenvector-centrality\tcompute eigenvector centrality
   centrality\t\t\tcompute all centrality values (depending on whether the graph is directed or not)
   modularity\t\t\tpreform community detection

If no command is inputted, default behanvior will compute all of the above.

Use -h or --help to show usage information.
   ''' % (name)

def validateFile(file_name):
   return True

def formatErrorAndExit(message):
   print 'ERROR: %s' % (message)
   print '(Use -h or --help to show usage information.)'
   sys.exit(2)

def main(argv):
   try:
      opts, args = getopt.getopt(argv[1:],'n:e:i:o:gphd',['node-list=','edge-list=','ifile=','ofile=','gephi','help', 'directed'])
   except getopt.GetoptError:
      formatErrorAndExit('Invalid input options or arguments.')

   print opts
   print args

   gephi = False
   directed = False
   node_list = None
   edge_list = None
   input_file = None
   output_file = ('out', True)

   for opt, arg in opts:
      if opt in ('-h', '--help'):
         print formatUsage(argv[0])
         sys.exit(2)
      if opt in ('-g', '--gephi'):
         gephi = True
      elif opt in ('-d', '--directed'):
         directed = True
      elif opt in ('-n', '--node-list'):
         validateFile(arg)
         node_list = arg
      elif opt in ('-e', '--edge-list'):
         validateFile(arg)
         edge_list = arg
      elif opt in ('-i', '--ifile'):
         validateFile(arg)
         input_file = (arg, gephi)
         gephi = False
      elif opt in ('-o', '--ofile'):
         validateFile(arg)
         output_file = (arg, gephi)
         gephi = False

   G = None
   setting = getConfig()
   if input_file:
      print 'Loading graph %s' % input_file[0]
      if input_file[1]:
         G = construct.loadFromGephi(input_file[0])
      else:
         G = construct.loadGraph(input_file[0])
   elif edge_list or node_list:
      print 'Constructing graph'
      G = construct.buildGraph(edge_list, node_list, setting, directed)
   else:
      formatErrorAndExit('No input file, edge list or node list.')

   if args:
      for command in args:
         print 'Processing command: %s' % (command)
         if command == 'modularity':
            modularity.louvainModularity(G)

   if output_file:
      print 'Outputting to %s' % (output_file[0])
      if output_file[1]:
         construct.dumpToGephi(G, output_file[0])
      else:
         construct.dumpGraph(G, output_file[0])


if __name__ == "__main__":
   main(sys.argv)

