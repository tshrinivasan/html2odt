from readability.readability import Document
import urllib
import codecs

def convert_to_html(url,filename):
#url = "http://www.tamilpaper.net/?p=3652"
	html = urllib.urlopen(url).read()
	readable_article = Document(html).summary()
	readable_title = Document(html).short_title()

	output = codecs.open(str(filename) + ".html","w", "utf-8")

#readable_article = unicode(readable_article)
	output.write("<h2>" + readable_title + "</h2>")
	output.write(readable_article + "<hr/>")
	output.close()

count = 1
links = open("zen.links","r").readlines()

for link in links:
	convert_to_html(link,count)
	count = count + 1

