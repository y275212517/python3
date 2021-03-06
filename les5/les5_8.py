#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 偏函数

print(int('12345'))
print(int('12345', base = 8))
print(int('12345', 16))

def int2(x, base = 2):
    return int(x, base)

print(int2('1000000'))
print(int2('1010101'))

import functools

int21 = functools.partial(int, base = 2)
print(int21('1000000'))
print(int21('1010101'))

max2 = functools.partial(max, 10)
print(max2(5, 6, 7))
print(max2(5, 6, 7, 11))
