#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'getIdealNums' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. LONG_INTEGER low
#  2. LONG_INTEGER high
#

def isideal(n):
    while n>1:
        if n%3 == 0:
            n = n/3
        elif n%5 == 0:
            n = n/5
        else:
            return False
    if n == 1:
        return True
        

def getIdealNums(low, high):
    count = 0
    for n in range(low, high+1):
        if isideal(n):
            count += 1
    return count

if __name__ == '__main__':