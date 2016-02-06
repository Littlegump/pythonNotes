#/usr/bin/env python
import os
f1 = open('/etc/test.xt', 'w+')

for line in ( i**2 for i in range(1,11) ):
    f1.write(str(line)+'\n')


# jiang shuju cong huanchongqu xie dao cipan shang 
f1.flush()
f1.close()
