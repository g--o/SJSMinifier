# Import the os module, for the os.walk function
import os
import argparse

# Set  params from argv
parser = argparse.ArgumentParser(description='Compress js files into one js.')
parser.add_argument('startingDirectory', metavar='SD', type=str, help='The directory to start searching from.')
parser.add_argument('outputFile', metavar='OF', type=str, help='The path to output file.')
args = parser.parse_args()

rootDir = args.startingDirectory
outputFile = args.outputFile

x = ""
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname[-3:] == ".js":
            x += " " + dirName + "\\" + fname
os.system("release\\node_modules\\.bin\\uglifyjs.cmd " + x + " -o " + outputFile)
