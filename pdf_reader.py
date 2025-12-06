import pandas as pd
import re
from pypdf import PdfReader
reader = PdfReader("sample-in.pdf")
# print(reader.pages)
page=reader.pages[2]
ep=page.extract_text()
# p=r"Phone:(\s)(\+)([0-9]+)(\s)([0-9]+)(\s)([0-9]+)(\-)([0-9]+)"
# match=re.search(p,ep)
# print(match.group())
p=r"\S+"
match=re.finditer(p,ep)
# print(match)
for i in match:
    print(i.start(),i .end(),i.group())