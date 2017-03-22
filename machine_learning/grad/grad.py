#!/usr/bin/env python

step = 0.1
x = 2
f_change = x ** 2
f_current = x ** 2
while f_change > 0.000000001:
    x = x - step * 2 * x
    f_change = f_current - x ** 2
    f_current = x ** 2

print f_current
