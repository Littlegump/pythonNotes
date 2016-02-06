#/usr/bin/env python
# coding=utf8
# map(func,seq[,seq2])
# map函数调用“映射”到每个序列的对应元素上并返回一个含有所有返回值的列表

#也就是对对应位置的元素做了func处理之后，然后形成一个元组列表
#[(),(),(),]

l1 = [7, 1, 2, 3, 4, 5, 6]
l2 = ['Sun', 'Mon', 'Tue', 'Wed', 'Tur', 'Fri', 'Sat']

l3 = map(None,l1,l2)
print l3

def func(x):
    return x*2

l4 = map(func,l1)
print l4

l5 = map(func,l2)
print l5

def func2(x,y):
    return x*2, y*2

l6 = map(func2,l1,l2)
print l6
