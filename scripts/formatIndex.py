from pathlib import Path
from posixpath import basename, splitext
import os
import argparse

import re

parser = argparse.ArgumentParser()
parser.add_argument("inputFilename")
parser.add_argument("youtubeLink")
args = parser.parse_args()

inputFilename = args.inputFilename
youtubeLink = args.youtubeLink
outputFilename = "VideoIndex.js"

with open(inputFilename, "r") as sourceText:
  sourceLines = sourceText.readlines()

with open(outputFilename, "w") as outFile:
  outFile.write("document.write('\\")
  outFile.write("\n")
  for l in sourceLines:
    newL = re.sub("^(\d+):(\d+):(\d+)", f"<a href=\"{youtubeLink}?t=\\1h\\2m\\3s\">\\1:\\2:\\3</a>",l)
    newL = re.sub("^(\d+):(\d+)", f"<a href=\"{youtubeLink}?t=\\1m\\2s\">\\1:\\2</a>",newL)
    title = re.search(r'\(.*\)',l).group(0)
    title = re.sub(r"'",r"\\'",title)
    # newL = re.sub(r"\(.*\)'", r"",newL) # remove title
    newL = re.sub(r"'", r"\\'",newL)
    newL = re.sub("\((.*)\) (https?:.*)", r"<a href=\2>\1</a>",newL)
    outFile.write(newL.rstrip()+"<br>\\\n")
  outFile.write(r"')")
