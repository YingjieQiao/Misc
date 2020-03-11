#Assignment 5
"""
Created on Wed May  8 17:56:54 2019

@author: danielqiao
"""

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Retrieve xml data using urllib
url = 'http://py4e-data.dr-chuck.net/comments_228552.xml'
stuff = urllib.request.urlopen(url, context=ctx).read()
data = ET.fromstring(stuff)
print(type(data))

lst = data.findall('comments/comment')
print(len(lst))
s = 0 
for item in lst:
    s += int(item.find('count').text)
print(s)

