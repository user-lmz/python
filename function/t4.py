#!/usr/bin/env python3

def sanjiao(n):
    L = [1]
    while True:
        yield L
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
        L.insert(0,1)
        L.append(1)
        if len(L)>n:
            break
    return 'Done'

g = sanjiao(10)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break

