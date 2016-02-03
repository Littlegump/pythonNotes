#/usr/bin/env python

import os
fileList1 = os.listdir('/var/log')

fileList2 = [ i for i in fileList1 if i.endswith('.log') ]

print fileList2,
