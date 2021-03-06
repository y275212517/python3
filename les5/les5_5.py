#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 返回函数

# 通常的可变参数的求和函数
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax
# 如果不需要立即求和
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax += n
        return ax
    return sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)
print(f())

# 上面的这个称为闭包
'''
lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”
的程序结构拥有极大的威力。
请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数
'''

def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
'''
期望结果 1, 4, 9
结果全是9
全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，
因此最终结果为9。
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
'''

def count1():
    def f(j):
        def g():
            return j * j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())
