#Assignment: Extracting Data With Regular Expressions
"""
Created on Mon May  6 15:21:32 2019

@author: yingjie_qiao
"""

import re

pattern = re.compile(r'\d+')
s = 0

with open('regex_sum_228548.txt') as f:
    content = f.read()
    thelist = re.findall(pattern,content)
    for num in thelist:
        s += int(num)
    print(s)