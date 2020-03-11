#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 20 14:59:32 2019

@author: danielqiao
"""
import random

nums = [i for i in range(1,10)]

def generate_spaces(ss):
    ss = [[a,b,0] for a in range(3) for b in range(3)]
    return ss

def fill(ss):
    sss = []
    for n in nums:
        s = random.choice(ss)
        s[2] = n
        sss.append(s)
        ss.remove(s)
    return sss

def hor_check(ss):
    sums = []
    i = 0
    while i <= 2:
        S = 0
        for s in ss:
            if s[0] == i:
                S += s[2]
        sums.append(S)
        i += 1
    if sums[0] == sums[1] and sums[0] == sums[2]:
        return sums[0]
    else:
        return 999
    
def ver_check(ss):
    sums = []
    i = 0
    while i <= 2:
        S = 0
        for s in ss:
            if s[1] == i:
                S += s[2]
        sums.append(S)
        i += 1
    if sums[0] == sums[1] and sums[0] == sums[2]:
        return sums[0]
    else:
        return 9999

def dia_check(ss):
    s1 = []
    sum1 = 0
    for s in ss:
        if s[0] == 0 and s[1] == 0:
            s1.append(s[2])
        elif s[0] == 1 and s[1] == 1:
            s1.append(s[2])
        elif s[0] == 2 and s[1] == 2:
            s1.append(s[2])
    sum1 = sum(s1)
    
    s2 = []
    sum2 = 0
    for s in ss:
        if s[0] == 0 and s[1] == 2:
            s2.append(s[2])
        elif s[0] == 1 and s[1] == 1:
            s2.append(s[2])
        elif s[0] == 2 and s[1] == 0:
            s2.append(s[2])
    sum2 = sum(s2)
    if sum1 == sum2:
        return sum1
    else:
        return 99999


        


m = True
while m:
    try:
        def find_solution():
            spaces = []
            spaces = generate_spaces(spaces)
            spaces = fill(spaces)
            a = hor_check(spaces)
            b = ver_check(spaces)
            c = dia_check(spaces)
            if a == b == c:
                print(spaces,a)
                global m
                m = False
        find_solution()
    except RecursionError:
        pass
    