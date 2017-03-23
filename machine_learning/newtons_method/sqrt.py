#!/usr/bin/env python

n = 1
x = 1 
y = 9
while abs(x ** 2 - y) > 0.03:
    x = 0.5 * (x + n / x)
    n = n + 1
    print x

print x
