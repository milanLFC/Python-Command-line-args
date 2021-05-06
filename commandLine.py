import os, sys, getopt

listOfFilesFile = ''
outputfile = ''

def checkArguments(argv):
   global outputfile
   global listOfFilesFile

   if len(argv) != 2:
      print('wrong number of parameter')
      print('usage: ' + scriptName + ' -i <listOfFilesFile> ')
      exit()
   try:
      #opts, args = getopt.getopt(argv,"hi",["ifile="])
      opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      #print(scriptName + ' -i <listOfFilesFile> ')
      print(scriptName + ' -i <listOfFilesFile> -o <outputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         #print(scriptName + ' -i <listOfFilesFile>')
         print(scriptName + ' -i <listOfFilesFile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         listOfFilesFile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
   print('Input file is ' + listOfFilesFile)
   print('Output file is ' + outputfile)

if __name__ == "__main__":

   scriptName = os.path.basename(__file__)
   checkArguments(sys.argv[1:])
   print('Input file is ' + listOfFilesFile)
   print('Output file is ' + outputfile)

