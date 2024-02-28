#1
import re
with open("row.txt", 'r') as f:
    content=f.read()
    if re.search("EU", content):
        print()
        print (re.findall("EU", content))





