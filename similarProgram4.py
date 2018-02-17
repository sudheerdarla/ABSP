import re

from itertools import groupby

text = '''Find common typos such as multiple spaces between  words, 
accidentally accidentally repeated words, 
or multiple exclamat   ion marks at at the end of sentences. 
Those are annoying!!!'''

typoRegex = re.compile(r'\s{2,}|\w+|!{2,}')

mo = typoRegex.findall(text)

mo = " ".join(mo)

ntext = " ".join([k for k,v in groupby(mo.split())])

print(ntext)


