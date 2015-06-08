# -*- coding: utf-8 -*-
"""
Created on Mon Jun 08 15:01:25 2015

@author: 12T5062G
"""

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print word