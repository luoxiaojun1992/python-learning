#!/usr/bin/env python

step = 0.1
y = 9
x = y
while x ** 2 - y > 0.21:
    x = x - step * 2 * x
    print x

print x
