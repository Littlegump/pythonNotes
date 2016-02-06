#/usr/bin/env python
#coding=utf8

# reduce(func,seq[, init])


def func(x,y):
    return x+y

l1 = [0,1,2,3,4,5]

l2 = reduce(func,l1)

print l2
