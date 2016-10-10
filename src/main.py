import sys, getopt
import ConfigParser

from construct import *
from centrality import *
from modularity import *

def getConfig():
   config = ConfigParser.ConfigParser()
   config.read('../config.cfg')
   return config

def formatUsage(name):
   return '''
      %s -n <node-list-file> -e <edge-list-file> -i <input-graph-object-file> -o

   ''' % (name)

def main(argv):
   try:
      opts, args = getopt.getopt(argv[1:],'neiog:',['node-list=','edge-list=','ifile=','ofile=','gephi'])
   except getopt.GetoptError:
      print 'test.py -i <inputfile> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -i <inputfile> -o <outputfile>'
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print 'Input file is "', inputfile
   print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv)

