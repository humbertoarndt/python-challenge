# ==============================================================================
# Imports
# ==============================================================================
from challenge_imports import string
from challenge_utils import print_html

# ==============================================================================
# Challenge #01 - What about making trans?
# ==============================================================================
print('>> Challenge #01')

# First Solution - Without maketrans()
text = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
n_text = ''

for c in text:
    if c.isalpha():
        letters = string.ascii_lowercase
        index =  letters.index(c)
        if c == 'y':
            n_text += letters[0]
        elif c == 'z':
            n_text += letters[1]
        else:
            n_text += letters[index + 2]
    else:
        n_text += c
print(n_text)

# Second Solution - With maketrans()
int = 'abcdefghijklmnopqrstuvxwyz'
out = 'cdefghijklmnopqrstuvxwyzab'
table = str.maketrans(int, out)
print(f'\n{text.translate(table)}\n')

# http://www.pythonchallenge.com/pc/def/map.html
url = 'map'
print_html(url.translate(table))