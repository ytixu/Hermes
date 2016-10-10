import sys, getopt
import ConfigParser

def getConfig():
   config = ConfigParser.ConfigParser()
   config.read('../config.cfg')
   return config

def formatUsage(name):
   return '''Usage:
   %s -n <node-list-file> -e <edge-list-file> -i <input-graph-object-file> -o

   ''' % (name)

def main(argv):
   try:
      opts, args = getopt.getopt(argv[1:],'n:e:i:o:g',['node-list=','edge-list=','ifile=','ofile=','gephi'])
   except getopt.GetoptError:
      print formatUsage(argv[0])
      sys.exit(2)

   print opts
   print args
   # for opt, arg in opts:
   #    if opt == '-h':
   #       print formatUsage(argv[0])
   #       sys.exit()
   #    elif opt in ("-i", "--ifile"):
   #       inputfile = arg
   #    elif opt in ("-o", "--ofile"):
   #       outputfile = arg
   # print 'Input file is "', inputfile
   # print 'Output file is "', outputfile

if __name__ == "__main__":
   main(sys.argv)

