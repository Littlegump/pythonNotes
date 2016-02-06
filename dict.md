##创建字典，赋值
d1 = {}
d1['x'] = 123

dict()工厂函数来创建
dict3 = dict((['x',1],['y',2]))

##字典值的访问
for key in dict3:
    print key,dict3[key]

for i in dict3.keys():
    print 'keys=%s, value=%s' % (key, dict3[key])

dict['y'] = 'sdf'
##字典值的更新

dict.update(dict2)

##删除
del dict2['name']
dict2.clear()  shanchu dict2中的所有条目
del dict2 删除整个dict2字典
dict2.pop('x') 删除并返回key='x'的条目

