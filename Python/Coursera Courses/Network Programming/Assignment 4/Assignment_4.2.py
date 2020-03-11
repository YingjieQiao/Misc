#Assignment 4
"""
Created on Tue May  7 15:04:31 2019

@author: danielqiao
"""
def solution(url,position):
    
    import urllib
    from bs4 import BeautifulSoup
    import ssl
    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    #Read the html file
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    #Get all the links on this site
    tags = soup('a')
    
    i = 0
    for tag in tags:
        i += 1
        if i == position:
            thetag = tag
            break
    print(thetag)
    
    #Retrieve the link
    import re
    pattern = re.compile(r'href="(.+)"')
    templist = re.findall(pattern,str(thetag))
    x = ''
    for temp in templist:
        x += temp
    
    solution(x,position=18)
    #From here onwards, this function goes into an infinite loop.
    #I use 'ctrl+c' to force the loop to stop when I see the 7th line printed.
    #I should work out a way to stop the iteration here later.    
    
    
solution('http://py4e-data.dr-chuck.net/known_by_Ceejay.html',position=18)
    
