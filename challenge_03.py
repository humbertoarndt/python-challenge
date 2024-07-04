# ==============================================================================
# Imports
# ==============================================================================
from challenge_imports import os
from challenge_imports import re
from challenge_imports import urllib
from challenge_utils import print_php

# ==============================================================================
# Challenge #03 - re
# ==============================================================================
print('>> Challenge #03')

# Creating file
url = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--([\w\n]*?)-->", url, re.DOTALL)[-1]
filename = 'resources/re.txt'
if not os.path.exists(filename):
    with open(filename, 'w') as f:
        f.write(data)

# [a-z]: 1 lower case letter
# [A-Z]: 1 upper case letter
# [A-Z]{3}: 3 consecutive upper case letters
# [A-Z]{3}[a-z][A-Z]{3}: 3 upper case letters + 1 lower case letter + 3 upper case letters
# [^A-Z]: any character BUT an upper case letter
# [^A-Z]+: at least one such character
# [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+: something else before and after our patter(AAAbCCC) so there's no more than 3 consecutive upper case letters on each side
# [^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+: ...and we only care about the lower case
target = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"

# Searching pattern in the file
with open(filename, 'r+') as f:
    file_content = f.read()
    str = ("".join(re.findall(target, file_content)))
print_php(str)