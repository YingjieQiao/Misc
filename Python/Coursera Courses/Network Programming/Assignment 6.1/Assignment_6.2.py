#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 11 15:35:36 2019

@author: danielqiao
"""

import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'SASTRA University'
parms = {}
parms['address'] = address
parms['key'] = 42
url = serviceurl + urllib.parse.urlencode(parms)
stuff = urllib.request.urlopen(url, context=ctx)
data = stuff.read().decode()

js = json.loads(data)

print(json.dumps(js, indent=4))
