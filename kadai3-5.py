# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:37:16 2015

@author: 12T5062G
"""

plus = '+'
minus = '-'
bar = '|'
space = ' '
        
def print_bar(bar,space):
    print bar,
    print space,
    print space,
    print space,
    print space,
    print bar,
    print space,
    print space,
    print space,
    print space,
    print bar  
    
def print_side(plus,minus):
    print plus,
    print minus,
    print minus,
    print minus,
    print minus,
    print plus,
    print minus,
    print minus,
    print minus,
    print minus,
    print plus


def print_spam(minus,plus,space,bar):
    print_side(plus,minus)
    print_bar(bar,space)
    print_bar(bar,space)
    print_bar(bar,space)
    print_bar(bar,space)
    print_side(plus,minus)
    print_bar(bar,space)
    print_bar(bar,space)
    print_bar(bar,space)
    print_bar(bar,space)
    print_side(plus,minus)
    
print_spam(minus,plus,space,bar)

