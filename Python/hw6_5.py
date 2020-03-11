#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 15:48:52 2019

@author: danielqiao
"""

from math import sin
from math import cos
from math import tan

global x
x = 2.2

for i in range(30):
    f = (x/sin(x/2))-2.5
    print("f(x)=" + str(f))
    f1 = ((2*tan(x/2))-x)/sin(x)
    print("f1(x)=" + str(f1))
    x = x - f/f1
    print("x=" + str(x))
    print("\n")



print("-------------------")

global t
t = 2.2

for i in range(20):
    f = 16*t**2+50*cos(t)-50
    print("f(x)=" + str(f))
    f1 = 32*t-50*sin(t)
    print("f1(x)=" + str(f1))
    t = t - f/f1
    print("t=" + str(t))
    print("\n")
    
    
    
    
