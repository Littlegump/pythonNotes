<center>Python笔记之（列表）</center>
==================

##列表的初始化
##列表的访问
##列表的更新
##列表或列表元素的删除

序列类型操作符
##切片 ([ ]和[ : ])
        不仅可以在切片的结果上再进行切片，还可以改变切片的结果
##成员关系操作
        in, not in
##链接操作符（+）
        list1 = ...
        list2 = ...
        list1 + list2
        他和extend()的区别：
        普通链接操作符是创建一个新的list
        extend()方法是把新列表添加到原来的列表里面，而不是创建一个新列表
##重复操作符（*）

##列表类型操作父和列表解析(后面会有详解)
        [ i * 2 for i in [8, -2, 5]]
            [16, -4, 10]
        [ i for i in range(8) if i % 2 == 0 ]
            [0, 2, 4, 6]

##内建函数

###标准内建函数
        cmp()
###序列类型函数
        len()
        max()
        min()
        sorted() and reversed()
        enumerate() and zip()
        sum()
        list() and tuple

###列表类型内建函数（方法）
        使用dir()来获对象的方法和属性------dir(list)
        list.append(obj)
        list.count(obj)
        list.extend(seq)
        list.index(obj, i, j) //在list的i索引位到j索引位查找obj对象，如果有，显示其索引值。通常i=0,j=len(lsit)
        list.insert(index,obj)
        list.pop(index=-1) //删除并且返回指定索引位的对象
        list.remove()
        list.reverse()
        list.sort(func=None,key=None,reverse=False)//这个还没有试，下去再看看。
        
        使用index来查找某个obj是否在list中
        
        for eachMedia in ('a', 'b', 'c'):
            if eachMedia in music_media:
                print music_media.index(eachMedia)
                
###可以改变对象值的可变对象的方法是没有返回值的，不可变对象的方法是不能改变他们的值的，所以他们呢必须返回一个新的对象。

###用列表构建数据结构（堆栈和队列）