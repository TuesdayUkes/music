from pathlib import Path
from posixpath import basename, splitext
import os

# lambda l accepts a path and returns just the filename without an extension
l = lambda p: str(os.path.splitext(os.path.basename(p))[0])

allFiles = []
# for p in Path("./").rglob('*.chopro'):
#   allFiles.append(p)
# 
# for p in Path("./").rglob('*.cho'):
#   allFiles.append(p)

for p in Path("./").rglob('*.pdf'):
  allFiles.append(p)

sortedFiles = sorted(allFiles, key=(lambda p: l(p).casefold()))

htmlOutput = open("PDFLinks.html", "w")
for f in sortedFiles:
  htmlOutput.write(f"<a href=\"{str(f.resolve())}\" download>{l(f)}</a><br>")
