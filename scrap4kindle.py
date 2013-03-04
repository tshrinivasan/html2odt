from readability.readability import Document
import urllib
import codecs

def convert_to_html(url,filename):
	html = urllib.urlopen(url).read()
	readable_article = Document(html).summary()
	readable_title = Document(html).short_title()

	output = codecs.open(str(filename) + ".html","w", "utf-8")

	output.write("<h2>" + readable_title + "</h2>")
	output.write(readable_article + "<hr/>")
	output.close()

count = 1
links = open("links.txt","r").readlines()

for link in links:
	convert_to_html(link,count)
	count = count + 1

