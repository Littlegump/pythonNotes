#/usr/bin/env python

import os

f1 = open('/tmp/write.txt', 'w+')

l1 = os.listdir('/etc')

l2 = [ filename+'\n' for filename in l1 ]

f1.seek(0)

f1.writelines('www.baidu.com')

f1.flush()

f1.close()
