"""
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 
1**1 + 2**2 + 3**3 + ... + 1000**1000.
"""

import time

last10 = 0
modulo = int(10e10)

t1=time.time()
for ii in range(1,1001):
    last10 += ii**ii
t2=time.time()

print str(last10)[-10:], t2-t1
#9110846700

last10 = 0
t1=time.time()
for ii in range(1,1001):
    tmp = (ii**ii) % modulo
    last10 = (last10+tmp) % modulo
t2=time.time()

print str(last10)[-10:], t2-t1
