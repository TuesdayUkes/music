from pathlib import Path
from posixpath import basename, splitext
import os

# lambda l accepts a path and returns just the filename without an extension
l = lambda p: str(os.path.splitext(os.path.basename(p))[0])
ext = lambda p: str(os.path.splitext(os.path.basename(p))[1])


# for p in Path("./").rglob('*.chopro'):
#   allFiles.append(p)
# 
# for p in Path("./").rglob('*.cho'):
#   allFiles.append(p)

with open("scripts/HTMLheader.txt", "r") as headerText:
  header = headerText.readlines()

allFiles = []
for p in Path("./").rglob('*.pdf'):
  allFiles.append(p)
for p in Path("./").rglob('*.chopro'):
  allFiles.append(p)

def findMatchingBasename(files, basename):
  matches = [f for f in files if f[0].lower() == l(basename).lower()]
  if matches:
    return matches[0]
  else:
    return None

allTitles = []
for p in allFiles:
  matchingTitle = findMatchingBasename(allTitles, p)
  if matchingTitle:
    # print(matchingTitle)
    matchingTitle.append(str(p))
  else:
    allTitles.append([l(p), str(p)])

sortedTitles = sorted(allTitles, key=(lambda e: e[0].casefold()))
with open("PDFLinks.html", "w") as htmlOutput:
  htmlOutput.writelines(header)
  htmlOutput.write("<table>")
  for f in sortedTitles:
    try:
      htmlOutput.write("<tr>")
      htmlOutput.write(f"  <td>{f[0]}</td>\n<td>")
      for i in f[1:]:
        htmlOutput.write(f"  <a href=\"{str(i)}\" download>{ext(i)}</a>\n")
      htmlOutput.write("</td></tr>\n")
    except:
      print(f"failed to write {f[1:]}")

  htmlOutput.write("</table>")

  htmlOutput.write("</div>\n")
  htmlOutput.write("</div>\n")
  htmlOutput.write("</body>\n")


# sortedFiles = sorted(allFiles, key=(lambda p: l(p).casefold()))
# 
# with open("PDFLinks.html", "w") as htmlOutput:
#   htmlOutput.writelines(header)
#   for f in sortedFiles:
#     htmlOutput.write(f"  <a href=\"{str(f)}\" download>{l(f)}</a><br>\n")
#   htmlOutput.write("</div>\n")
#   htmlOutput.write("</div>\n")
#   htmlOutput.write("</body>\n")
# 
