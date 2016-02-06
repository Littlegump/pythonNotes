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

#迭代器
##What is 迭代器
序列类型：list,str,tuple
非序列类型：dict,file
自定义的有__iter__方法或者__getiter__的类型
都是可迭代对象
##Python的列表解析,比for循环速度快一倍的速度来根据已有的列表生成新列表的方式，
	语法结构：[expression for iter_var in iterable]
    ```	
	l1 = [1,2,3,4,5,6]
	l2 = [ i**2 for i in l1 ]
    ```

	[expression for iter_var in iterable if cond_expr]
	
    ```	
	l1 = [1,2,3,4,5,6]
	l2 = [ i**2 for i in l1 if i >= 3]
    ```
##Python的生成器表达式，每一个生成器对象都会生成一个新的迭代器对象,生成器一次只能生成（返回）一个对象，对象每次计算出一个条目后，把这个条目“产生”（yield）出来。
	(expression for iter_var in iterable)
	(expr for iter_var in iterable if cond_expr)

	g1 = 

## 产生偏移和元素
	range(1,101,2)
	跳跃式索引
	enumerate()函数可以生成基于数字键的字典，产生结果为元组，返回索引和元素本身
'''
	url = 'www.baidu.com'
	g1 = enumerate(url)
	g1.next()
'''

#文件（FILE）
------------
###Python的open()函数用于打开文件和创建文件对象
	open(name [,mode[, buffersize]])
	文件存储有两种方式，文本文件，二进制文件
	mode指定文件的打开模式
	    r:只读模式
	    open('/var/log/message.log','r')
	    w:写入
	    a:附加模式，不会覆盖原来文件，而是在文件末尾添加
	    在模式后使用“+”，表示同时支持读入写入方式,以只读模式打开文件，可以写，这主要针对w默认会创建一个文件，使用r+可以防止用户创建一个没有的文件。
		r+,w+,a+
	    在模式后加"b"，表示使用二进制方式打开该文件
		rb,wb,ab,rb+,wb+,ab+
	bufsize	:定义输出缓冲
	    0表示禁用患处
	    负数：使用系统默认缓冲
	    1：只缓冲一行数据
	    2+：指定缓冲空间大小

	help(file)
	如何创建一个文件对象

	```
	f1 = open('/etc/passwd','r')
	f1.next() 使用next不会移动文件指针，readline会移动。
	f1.close()
	f1.fileno()：返回其文件描述符(简单的小整数，用来引用打开的文件,基本都是大于三的，因为标准输入，标准输出，标准错误输出把012占用了)
	f1.readline()：从文件中读取并返回一个对象，包括行结束符
	f1.readlines()，返回一个列表形式返回所有行，每一行表示一个列表元素。
	f1.tell(),返回当前如何知道readline的指针位置?
	f1.seek(offset [, whence])如何移动指针。0默认表示从文件头部开始偏移，1表示从当前位置开始偏移，2表示从文间尾部开始偏移，offset表示要偏移的数量.
	如：f1.seek(0) 通过此方法将文件移动到自己所想要移动的位置
	加入要偏移到第二行就直接用next()函数
	f1.read(size)：直接指定要从文件中读取多少字节数	
	    f1 = open('/etc/[passwd','r')
	    f1.read(10)
	    f1.next()
	f1.name  返回文件的文件名，他是一个属性，不是方法。用于调用当前文件的名称	
	f1.write() 
	f1.writelines() 必须是字符序列，或者将一个list传递到里面，将返回所有列表元素链接而成的字符串。
	例：
	f1 = open('/etc/test1.txt','w+')
	l1 = os.listdir('/etc') 
	l2 = [ filename+'\n' for filename in l1 ]
	f1.seek(0)
	f1.writelines(l2)
	f1.flush()
	f1.close()

	f1.xreadlines() 用于实现向后兼容的，基本废弃
	
	f4.isatty() 是否是一个终端tty
	
	f4.truncate() 做文件截取
		f4.truncate(100) 截取之后只保留100个字节
		f3.truncate(f4.tell())截取到当前文件指针的位置
	f4.closed用于判断当前文件是否为关闭的状态。这个是一个属性，不是方法
	f4.encoding
	f4.mode获取当前文件的打开模式
	f4.newlines 返回到读取到的行分隔符的字串位置,如果有其他换行符会显示
	f4.softspace 软空间，0表示不用空间分隔符*****

# OS模块
-------
如何在某个目录下创建一个目录，目录是文件系统的组成部分，不是文件内容的组成部分。使用OS模块来实现Python来实现和文件系统交互。
os就是系统api

os.mkdir(path [, mode=0777]) //创建一个目录
os.getcwd()获取当前工作目录  
os.chdir('/tmp')  相当于cd命令。
os.chroot()设定当前进程的root
os.listdir（）列出指定目录下的所有文件名
os.mkdirs( ) 相当于-p
例如：os.mkdirs('x/y/z')在当前目录下创建多级目录
os.rmdir() 删除目录
os.removedirs（）删除多层目录

文件：
    mkfifo()创建米名管道
    mknod()创建设备文件
    remove()用于删除文件
    unlink()
    rename（）
    stat() 返回文件的状态信息
    symlink()创建符号链接 os.symlink('test2.txt','test2.syslink')
    utime()用于更新文件的时间戳
    tmpfile() 创建并打开一个临时的新文件

os.walk（top, d）目录树生成器，相当于tree
例如：g1 = os.walk('/tmp')
g1.next()

访问权限：

	os.access（）用于检验指定用户对文件是否有访问权限
	os.access('/tmp/test.xtx',0)检验管理员是否有访问该文件的权限

	os.chmod('test2.txt',0640)
	修改文件的权限

	os.chown(path,uid,gid)
	os.umask(默认的文件遮罩码)

文件描述符：
	os.open()： 底层操作系统模块，
	os.read()
	os.write()

设备文件：
	mkdev(主设备号，此设备号)
	mkjor()获取设备的设备号码
	minor()****


还有一个子模块
	os.path.×××实现文件路径名，那个字符串的修剪，也就是和文件路径操作相关的模块
	basename() 文件基名
	dirname() 路径目录名
	join()将多个离散路径合并成一个完整的路径
		dir1 = os.path.dirname('/etc/sysconfig/network-scripts')
		file1 = os.path.basename(/etc/sysconfig/network-scripts)
		print dir1 file1
		os.path.join(dir,file1)
		
		os.listdir('/tmp')
		for filename in os.dirlist('/tmp'):
			print os.path.join('/tmp', filename)


	os.path.split()返回dirname和basename 的元组对象
	os.path.
	os.path.splitext()返回filename和extension元组，将文件名和扩展名分开
	os.path.getatime()
	os.path.getctime()
	os.path.getmtime()
	os.path.getsize()返回文件的大小
	判断类操作
	os.path.exists() 判断指定文件是否存在
	os.path.isabs() 判断指定的路径是否为绝对路径
	os.path.isdir() 判断指定位置是否为目录
	os.path.file() 是否存在且为文件
	os.path.link()
	os.path.ismount(): 是否为挂载点
	os.path.samefile(): 两个路径是否指向了同一个文件。

##对象文件流式化
特殊的对象写入文件的时候要对该对象做（流式化）处理，功能描述叫对象的持久存储。
要实现持久就要涉及pickle模块，marshal模块，DBM模块，shelve模块
例如：pickle模块，将python的原生对象存到文件中

	import pickle
	pickle.dump（obj,file)将某个对象dump到file中
	dict1 = {}
	file5 = open()
	pickle.dump(dict1,file5)
	f5.flush()
	f5.close()
	f6 = open(另一个文件准备装载)
	dict2 = pickle.load(f6)
	print dict2



