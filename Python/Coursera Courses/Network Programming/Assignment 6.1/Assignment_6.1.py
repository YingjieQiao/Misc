#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:21:04 2019

@author: danielqiao
"""

import json
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#Retrieve json data using urllib
url = 'http://py4e-data.dr-chuck.net/comments_228553.json'
stuff = urllib.request.urlopen(url, context=ctx).read()
data = json.loads(stuff)

s = 0
for item in data['comments']:
    s += item['count']
print(s)