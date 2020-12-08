#!/usr/bin/env python3

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'

'''#first way
x = 6
b = fib(x)
i = 0
while i < x:
    print(next(b))'''
    
'''#second way
for n in fib(6):
    print(n)'''

#third way
g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
