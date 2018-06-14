
import difflib
from pprint import pprint
import nltk

text1 = "text1.txt"; text2 = "text2.txt"

html = difflib.HtmlDiff()

diff = difflib.Differ()

f = open("result.html","w+")

# use nltk to tokenize text into word list first before the comparison
content = html.make_file(nltk.word_tokenize(open(text1,"r").read()),nltk.word_tokenize(open(text2,"r").read()), context=True)

f.write(content)

f.close()

# use nltk to tokenize text into word list first before the comparison
pprint(list(difflib.context_diff(nltk.word_tokenize(open(text1,"r").read()),nltk.word_tokenize(open(text2,"r").read()),fromfile='text1.txt', tofile='text2.txt')))
