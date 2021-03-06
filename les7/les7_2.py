#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 类和实例

"""
由于类可以起到模板的作用，因此，可以再创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
通过定义一个特殊的__init__方法，再创建实例的时候，就把name, score等属性帮上去
注意：__inin__方法的第一个参数永远是self,表示创建的实例本身，因此，再__init__方法内部，
就可以把各种属性绑定到self,因此self就是指向创建的实例本身。有了__init__方法，在创建
实例的时候，就不能传入空的参数了，必须传入与__inti__方法匹配的参数，但self不需要传，
Python解释器自己会把实例变量传进去。

和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是
实例变量self,并且调用时不用传递参数
"""

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s : %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simposn', 59)
lisa = Student('Lisa Simpson', 88)

print('bart.name = ', bart.name)
print('bart.score = ', bart.score)
bart.print_score()

print('grade of Bart: ', bart.get_grade())
print('grade of Lisa: ', lisa.get_grade())
