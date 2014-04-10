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
import numpy as np

maxnumber = 1000000


def nextnum(n):
    if n==1:
        return 0
    elif n%2==0:
        return n/2
    else:
        return 3*n+1

def seqlen(n):
    cnt = 1
    while not n==1:
        n = nextnum(n)
        cnt +=1
    return cnt

def sievenum(n):
    if not knownmask[n]:
        newnum = nextnum(n)
    #    print newnum
        if newnum >= maxnumber:
            chainlen[n] = seqlen(n)
            knownmask[n] = 1
        elif not knownmask[newnum]:
            sievenum(newnum)
            chainlen[n] = chainlen[newnum] + 1
            knownmask[n] = 1

iternums = np.arange(3,maxnumber,2, dtype='int')
chainlen = np.zeros(maxnumber, dtype='int')
knownmask = np.zeros(maxnumber, dtype='bool')
knownmask[0] = 1

for nn in iternums[iternums]:
    print nn
    sievenum(nn)

print chainlen.index(max(chainlen)), max(chainlen)
# 837799