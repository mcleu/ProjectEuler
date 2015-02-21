# -*- coding: utf-8 -*-
#==============================================================================
# It can be seen that the number, 125874, and its double, 251748, contain
# exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
# contain the same digits.
#==============================================================================

def isperm(a,b,c,d,e,f):
    return sorted(str(a)) == sorted(str(b)) == sorted(str(c)) == sorted(str(d)) == sorted(str(e)) == sorted(str(f))

for tt in range(1,200000):
    if isperm(tt, 2*tt, 3*tt, 4*tt, 5*tt, 6*tt):
        print(tt)

#142857
