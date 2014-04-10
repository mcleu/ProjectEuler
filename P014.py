# -*- coding: utf-8 -*-
#===============================================================================
# The following iterative sequence is defined for the set of positive integers:
# 
# n  n/2 (n is even)
# n  3n + 1 (n is odd)
# 
# Using the rule above and starting with 13, we generate the following sequence:
# 
# 13  40  20  10  5  16  8  4  2  1
# 
# It can be seen that this sequence (starting at 13 and finishing at 1) contains
# 10 terms. Although it has not been proved yet (Collatz Problem), it is thought
# that all starting numbers finish at 1.
# 
# Which starting number, under one million, produces the longest chain?
# NOTE: Once the chain starts the terms are allowed to go above one million.
#===============================================================================
import time

def nextnum(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def seqlen(n):
    cnt = 1
    while not n==1:
        n = nextnum(n)
        cnt +=1
    return cnt

t1=time.time()
m=[]
iternums = range(3,1000000,2)
#for n in iternums:
#    m.append(seqlen(n))
#    if (n-1)%5000==0:
#        print n

#print iternums[m.index(max(m))], max(m)
#print time.time()-t1

# 837799