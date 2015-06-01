# -*- coding: utf-8 -*-
"""
Created on Mon Jun 01 23:56:54 2015

@author: 12T5062G
"""

def print_index(fruit):
    index = len(fruit)
    while 0 < index:
        letter = fruit[index-1]
        print letter
        index = index - 1
        
def prefixes():
    prefixes = 'JKLMNOPQ'
    suffix = 'ack'
    for letter in prefixes:
        if letter =='O' or letter == 'Q':
            print letter + 'u' + suffix
        else:
            print letter + suffix
            
def find(word, letter,index):
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


def counter(word,char):
    count = 0
    print char
    find(word,char,count)
    print count

name = 'banana'
print name.count('a')

#print counter('interesting','i')
#print find('interesting','i',5)
#prefixes()
#print_index('orange')
#print_index('banana')