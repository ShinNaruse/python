# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:51:25 2015

@author: 12T5062G
"""

"""以下の関数 is_between(x, y, z)を書け。ここでx ≤ y ≤ zなら True
を返し、これ以外ならばFalse を返す。"""
def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

print is_between(1, 1, 1)#T
print is_between(1, 2, 2)#T
print is_between(1, 2, 3)#T
print is_between(1, 3, 2)#F
print is_between(2, 1, 1)#F
print is_between(2, 1, 2)#F
print is_between(2, 2, 3)#T
print is_between(3, 2, 1)#F



