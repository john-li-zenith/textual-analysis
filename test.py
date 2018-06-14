
import difflib
from pprint import pprint

text1 = "text1.txt"; text2 = "text2.txt"

# initiate HtmlDiff class
html = difflib.HtmlDiff()

# create a file handler to save html string returned by HtmlDiff instance
f = open("result.html","w+")

content = html.make_file(open(text1,"r").read(),open(text2,"r").read(), context=True)

# save the html to the file
f.write(content)

f.close()

# use context_diff to display the difference in the console
pprint(list(difflib.context_diff(open(text1,"r").read(),open(text2,"r").read(),fromfile='text1.txt', tofile='text2.txt')))
