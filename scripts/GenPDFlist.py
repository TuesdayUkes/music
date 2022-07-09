from pathlib import Path
from posixpath import basename, splitext
import os

# lambda l accepts a path and returns just the filename without an extension
l = lambda p: str(os.path.splitext(os.path.basename(p))[0])


# for p in Path("./").rglob('*.chopro'):
#   allFiles.append(p)
# 
# for p in Path("./").rglob('*.cho'):
#   allFiles.append(p)

with open("scripts/HTMLheader.txt", "r") as headerText:
  header = headerText.readlines()

allPdfFiles = []
for p in Path("./").rglob('*.pdf'):
  allPdfFiles.append(p)

sortedFiles = sorted(allPdfFiles, key=(lambda p: l(p).casefold()))

with open("PDFLinks.html", "w") as htmlOutput:
  htmlOutput.writelines(header)
  for f in sortedFiles:
    htmlOutput.write(f"<a href=\"{str(f.resolve())}\" download>{l(f)}</a><br>\n")
  htmlOutput.write("</body>\n")
