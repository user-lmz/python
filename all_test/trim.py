#!/usr/bin/env python3

def trim(s):
    length = len(s)
    if length > 0:
        for i in range(length):
            if s[i] != ' ':
                break
        j = length-1
        while(s[j] == ' ' and j >= i):
            j -= 1
        s = s[i:j+1]

    return s

m = trim(' abc df ')
print(m)
