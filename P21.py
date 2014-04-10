"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n
which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
55 and 110; therefore d(220) = 284. The proper divisors of 284 are
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import numpy as np
from time import time



def d(n):
    dsum = 1 # We start at 1 because we skip 1
    # We only need to test up to the root of the number (eg80, test for factors up to 8)
    maxnum = int(np.sqrt(n))
    # For cases where n is a perfect square, we only want to add it once
    if maxnum*maxnum == n:
        dsum = 1+ maxnum
    # Iterate through other factors
    for ii in xrange( 2, maxnum):
        #print 'cntupto', int(np.ceil(np.sqrt(n))), ii
        if n%ii == 0:
            #print ii, n/ii
            dsum += ii + n/ii
    return dsum



t1 = time()
pair=0
asum = 0
for nn in xrange(3,10000):
    pair = d(nn)
    if (pair > nn) and (pair<=10000):
        if d(pair)==nn:
            asum += nn + pair
        

print asum, t1-time() # 31626 -0.142999887466