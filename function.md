<center>#函数</center>
=====================

##Python中可以创建4种函数
-----------------------

- 全局函数： 定义在模块中  
- 局部函数： 嵌套在其他函数中  
- lambda： 表达式，匿名函数。  
- 方法： 与特定数据类型相关的函数，并且只能与数据类型关联一起使用，就是定义在类中的函数  

##Python内置函数


##创建函数  
    def functionName(parameters):  
		suite  

	def是一个可执行语句  
	def是一个对象，并将其赋值给一个变量名（即函数名）  

##名称空间

	一个变量所能生效的范围叫名称空间  
	函数内部的变量如果不特殊声明，他的作用域就是函数内部。  
	如果在函数变量名前加global就明确了全局变量的调用  
	
def f1():
...     global x
...     x = 2
...     print x


##变量名解析：lEGB原则
	built-in(Python)
		Python(module)
    		enclosing function locals
				local(function)

##函数中嵌套变量：

##闭合函数（工厂函数）
		#/usr/bin/env python
		def f1():
		    x = 3
		    def f2():
        		y = 'hello'
		        print x, y
		    return f2

		f1()

		a1 = f1()

		type(a1)

		a1()
		例2
		def f1(x)
			def f2(y)
				return y ** x
			return f2

		f3 = f1(4)
		f3(2)
		16

##尽量避免在函数内部修改外部的可变对象，比如列表和字典

		l1 = [1, 2, 3]
		def f5(x):
			x.pop()
			print x

		f5(l1[:])
		print l1
		可以使用副本复制的方式来进行操作，而不是直接调用，因为直接调用相当与浅复制

## 关键字参数，和位置参数（最原始的传参类型）,默认参数

		def f1(x,y):
			print x, y

		m = 4, n = 3

		f1(x=m, y=n)
	默认参数：
		def f8(x,y,z=9)
			print x, y, z
		f8()
	可变参数: 可以收集任意个参数，并返回元组
		def f10(*x)
			print x
		f10(m)
		f10(m, n)
		f10(m,6,9)

		用于收集关键字参数并返回字典。		
		def f11(**x)
			print x

		f11(x=1, y=2, z=3)
		
		混合
		def f12(*x,**y)
			print x
			print y

		f12(m,n,o,i=10,j=16)

## 变量的解析类型：
		变量的分解赋值
		l1 = ['abc','def','fff']
		x,y,z = l1

		def f17(x,y,z)
		    print x,y,z

		f17(*l1)

		定义是为了整合，调用是为了分解


## 匿名函数lambda: 用于定义短小的回调函数

		lambda x,y: x+y
		lambda args: expression 这个一定是一个表达式，而不是语句
		lambda x,y: print x, y 这个就是错的

		func1 = lambda x,y: x+y
		func1(1,2)
		
		l3 = [ (lambda x: x*2), (lambda y: y*3) ]
		for i in l3:
			print i(4)
		lambda表达式是被当作一个函数对象传递给for的i的，然后输出结果就是8 12


## 函数式编程，实现将函数作为参数传递给另一个函数，它仅仅是一种编程范式
		filter(func, seq)  过滤
			如
def f1(x):
	if x > 20 :
		return true
	else:
		return false

l1 = [1,2,33,54]

filter(f1,l1)

		map(func,seq1 [, seq2...])  折叠
		看map.py
		reduce(func, seq [, init])  映射
		看reduce.py

##python的闭包，叫lexical closure词法闭包，如闭合函数，内层函数所处的环境（环境就是外层函数），他所组成的整体叫闭包。
给内层函数提供运行环境

		例子：closure.py

			如果我们是一个棋盘 
		设计棋盘的位置不停在更新，但是有一个起始位置
			
		def startPosition(m,n):
			def newPosition(x,y):
				print "the old position is (%d,%d),and the new position is (%d,%d)." % (m,n,m+x,n+y)
			return newPosition
		
		action = startPosition(10,10)
		
		action(1,3)

		

## 列表解析生成器
		
		和上面的东西类似
		for i in (j**2 for j in range(1,11)): print i

## yield 生成器
		
		list((j**2 for j in range(1,11)))将生成器表达式转换为列表	
		有时候我们不想将生成器转换为列表。转换为更复杂的结构。
		列表解析生成器的施展空间有限。
		使用函数来实现生成器的效果：
			def genNum(x):
			    y = 0
			    while y <= x:
			    	yield y
			    	y += 1
			
			g1 = genNum(10)
			g1.next()

			def func(n):
			    i = 1
			    while i <= n:
				yield i ** 2
				i += 1
			g1 = func(20)
			for i in g1: print i
		函数中使用yield会返回一个生成器对象

## 范式编程
	
		装饰器：叫函数装饰器
		实现函数代码重用，函数功能在不同环境下的重用。插入日志，性能测试，
		1/装饰其本身是一个函数，用于装饰其他函数：
		2.功能：增强被装饰函数的功能

		装饰器一般接受一个函数对象作为参数，
		def decoration(func):
			def wrapper():
				print "hello,world"
				func()
				print "no zuo no die"
			return wrapper
		@decoration
		def show():
			return "I came from Mars."
	
		show()
		
		这个show函数本身只能说一句化，但是他却说了很多话，然后这个装饰器就叫做函数的装饰品
		例子2
		>>> def deco(func):
		...     def wrapper(x):
		...         print "aaaaaaaaaaaaaaaaa"
		...         func(x)
		...         print 'bbbbbbbbbbbb'
		...     return wrapper
		... 
		>>> @deco
		... def show1(x):
		...     print x
		... 
		>>> show('cao')	


			
## 递归函数：

		函数调用自身，不能陷入无线循环。
		递归需要边界条件，递归前段和递归返回段，一般递归不超过1000次
		如何做阶乘
		使用递归的方式写出更简洁的代码：
		10 × 9 × 8 × 7 × 。。。× 1
		10 * (10-1) * ((10-1)-1) * (((10-1)-1)-1)
		def func(n):
			if n<=1: return 1
			else: return n * func(n-1)
		func(3)

		func(3) = 3 * func(2)  = 3* 2 * func(1) = 3 * 2 * 1

## 携程：

## 函数的涉及规范：
		
		耦合性：
			尽可能不要让函数print太多东西，尽可能让函数接收参数，来适应更多场景，尽可能使用return来保证函数的独立性，
			尽量不要使用全局变量进行函数通信
			尽可能不要在函数中修改可变类型的参数
			尽量避免直接改变定义在另一个模块中的变量：
		聚合性：
			（1）每个函数都应该该有一个单一的统一的目标
			（2）每个函数的功能都应该相对简单。

