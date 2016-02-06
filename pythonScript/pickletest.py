#/usr/bin/env python
import pickle
d1 = {'name':'zhangsan', 'gender':'male', 'age':23}
print d1
file1 = open('/tmp/pickle.txt', 'w+') 
pickle.dump(d1, file1)
file1.flush()
file1.close()
file2 = open('/tmp/pickle.txt', 'r+')
d2 = pickle.load(file2)
print d2
l1 = [ i for i in d2 ]
print l1
