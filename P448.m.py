# -*- coding: utf-8 -*-
#==============================================================================
# The function lcm(a,b) denotes the least common multiple of a and b.
# Let A(n) be the average of the values of lcm(n,i) for 1<=i<=n.
# E.g: A(2)=(2+2)/2=2 and A(10)=(10+10+30+20+10+30+70+40+90+10)/10=32.
#
# Let S(n)=SUM A(k) for 1<=k<=n.
# S(100) 122726
# Find S(99999999019) mod 999999017.
#==============================================================================


from time import time
import numpy as np

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:
        a, b = b, a % b
    return a

def npgcd(a, b):
    a, b = np.broadcast_arrays(a, b)
    a = a.copy()
    b = b.copy()
    pos = np.nonzero(b)[0]
    while len(pos) > 0:
        b2 = b[pos]
        a[pos], b[pos] = b2, a[pos] % b2
        pos = pos[b[pos]!=0]
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def Sfast(nn):
    newsum = 0
    jj = nn
    while (jj > 0):
        #if jj%10==0:
        #    print '10 down'
        #print jj
        ii = jj
        while (ii > 0):
            newsum = (newsum + ii / gcd(ii,jj) ) % 999999017
            #print ii,jj #,gcd(ii,jj), ii / gcd(ii,jj)
            ii -= 1
        jj -= 1
    return newsum

def S2(nn):
    sum2 = 0
    jj = nn
    while (jj > 0):
        minisum = 0
        ii = nn
        while ( ii >= jj ):
            #print ii,jj
            minisum += 1.0 / gcd(ii,jj)
            ii -= 1
        sum2 += minisum * jj
        jj -= 1
    return int(sum2)


NN = 1200

t1=time()
print Svec(NN)
print time() - t1

t2=time()
print Sfast(NN)
print time() - t2

#Snew(100)