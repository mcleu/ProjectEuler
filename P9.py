#==============================================================================
# A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,
# 
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#==============================================================================


#a= 2mn; b= m^2 -n^2; c= m^2 + n^2;
#a + b + c = 1000;

#2mn + (m^2 -n^2) + (m^2 + n^2) = 1000;
#2mn + 2m^2 = 1000;
#2m(m+n) = 1000;
#m(m+n) = 500;
#
#m>n;
#
#m= 20; n= 5;
#
#a= 200; b= 375; c= 425;

import math

def find_triplet(Sum):
    m=0
    for n in xrange(Sum):
        delta = n**2 + 2*Sum
        m1 = (-n + math.sqrt(delta)) / 2
        m2 = (-n - math.sqrt(delta)) / 2
        if int(m1)==m1 and m1 > n:
            m = int(m1)
        elif int(m2)==m2  and m2 > n:
            m = int(m2)
        if not (m==0):
            return [2*m*n, m**2 - n**2, m**2 + n**2]
    return None

print find_triplet(1000)