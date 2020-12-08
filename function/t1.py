#!/usr/bin/env python3

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

m = add_end()
n = add_end()
print(m)
print(n)
