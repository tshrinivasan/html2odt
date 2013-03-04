When we need to read tamil books in kindle or any tablet device, 
epub or aws files are not supporting unicode.

But, all the devices can read pdf files, when the pdf files can have unicode content.

The internet has tons of contents.


We can copy the content from the html files and paste them in a libreoffice writer document.
set page size as 

9cm X 12 cm for 6" device
9cm X 15.5 cm for 7" device

set all margins as 0.5 cm

We have to copy only the main content leaving all the side widgets and advertisements.

It will be a tougher job to copy/paste the content.

This script will get the readable main content from the links in a file.
Will create one html file for one url.

We can merge all html files using the 'cat' command to create a single html file.

use 'xhtml2odt' to create a single odt file.


INSTALL:

1. Install readability-lxml
sudo easy_install readability-lxml

read more on this here
https://github.com/buriy/python-readability

2. Install xhtml2odt
http://xhtml2odt.org/

I got the deb file from here
http://download.opensuse.org/repositories/home:/abompard:/xhtml2odt/xUbuntu_11.04/all/

sudo dpkg -i  xhtml2odt_1.3-1_all.deb      



USAGE:

1. add the desired links in the text file "links.txt"

2. python scrap4kindle.py

This will generate many html files.

3. convert all the html files into single file

cat *.html > book.html

4. convert the file book.html into odt

xhtml2odt -i book.html -o book.odt

5. Now open the book.odt file.

select all the content using CTRL+A

set the font as "Lohit Tamil" and 9 points for tamil 

set the page size as 9cmX12cm and margins as 0.5 cm

save the file.

Export as PDF.

Now load the pdf into kindle or any ebook reader or any tablet device.

Enjoy the tamil reading.
































