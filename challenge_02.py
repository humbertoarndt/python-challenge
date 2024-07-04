# ==============================================================================
# Imports
# ==============================================================================
from challenge_imports import os
from challenge_imports import re
from challenge_imports import urllib
from challenge_utils import print_html

# ==============================================================================
# Challenge #02 -ocr
# ==============================================================================
print('>> Challenge #02')

# Creating file
url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
comments = re.findall("<!--(.*?)-->", url, re.DOTALL)
data = comments[-1]
filename = 'resources/ocr.txt'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write(data)

# Counting characters
c_count = {}
with open(filename, 'r') as f:
    while True:
        c = f.read(1)
        if not c:
            break
        if c in c_count:
            c_count[c] += 1
        else:
            c_count[c] = 1

# Identifying unique characters
s = str()
for char, count in c_count.items():
    if count == 1:
        s += char
print_html(s)