#Assignment 4: Scraping Numbers from HTML using BeautifulSoup
"""
Created on Tue May  7 14:42:17 2019

@author: danielqiao
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Retrieve the html file
url = 'http://py4e-data.dr-chuck.net/comments_228550.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

#Retrieve anchor tags
tags = soup('span')#Retrieve correspending part
print(soup)
s = 0
for tag in tags:
    s += int(tag.contents[0])
print(s)