# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:26:41 2015

@author: 12T5062G
"""

def square_root(a):
    x = 100.0
    epsilon = 0.0000001
    while True:
        print x
        y = (x + a/x) / 2
        if abs(y-x) < epsilon:
            break
        x = y

square_root(6.0)
square_root(5.0)
