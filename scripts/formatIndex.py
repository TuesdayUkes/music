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
JsFilename = "VideoIndex.js"
HtmlFilename = "VideoIndex.html"

with open(inputFilename, "r") as sourceText:
  sourceLines = sourceText.readlines()

with open(HtmlFilename, "w") as HtmlFile:
  with open(JsFilename, "w") as JsFile:
    JsFile.write("document.write('\\")
    JsFile.write("\n")
    for l in sourceLines:
      # For timestamps greater than an hour, look for three numbers separated by 2 colons
      newL = re.sub("^(\d+):(\d+):(\d+)", f"<a href=\"{youtubeLink}?t=\\1h\\2m\\3s\">\\1:\\2:\\3</a>",l)

      # For timestamps less than an hour, there are only two time fields (minutes : seconds)
      newL = re.sub("^(\d+):(\d+)", f"<a href=\"{youtubeLink}?t=\\1m\\2s\">\\1:\\2</a>",newL)

      # reshape URL for sheet music into an HTML tag using the song title as the
      # visible text
      newL = re.sub("\((.*)\) (https?:.*)", r"<a href=\2>\1</a>",newL)

      HtmlFile.write(newL.rstrip()+"<br>\n")

      # Add escape backslashes in front of single quotes (also used as apostrophe)
      # for the sake of the .js document.write string
      newL = re.sub(r"'", r"\\'",newL)

      JsFile.write(newL.rstrip()+"<br>\\\n")
    JsFile.write(r"')")
