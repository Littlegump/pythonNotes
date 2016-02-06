#/usr/bin/env python
#coding=utf8

# 将一个列表传递给filter，该列表中的元素满足func的元素将会被添加到一个新的列表中并作为filter的返回值，
# filter(func,seq)

l1 = [1,2,3,44,50]

def func(x):
    if x > 20:
        return True
    else:
        return False

l2 = filter(func,l1)
print l2

