# -*- coding: utf-8 -*-
#==============================================================================
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up
# of each of the digits 0 to 9 in some order, but it also has a rather
# interesting sub-string divisibility property.
# 
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
# note the following:
# d2 d3 d4  = 406 is divisible by 2
# d3 d4 d5  = 063 is divisible by 3
# d4 d5 d6  = 635 is divisible by 5
# d5 d6 d7  = 357 is divisible by 7
# d6 d7 d8  = 572 is divisible by 11
# d7 d8 d9  = 728 is divisible by 13
# d8 d9 d10 = 289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.
#==============================================================================

import itertools as it

def l2int(t):
    return int(''.join([str(i) for i in t]))

AllComb = it.permutations(['0','1','2','3','4','5','6','7','8','9'], 10)

DivList = [2,3,5,7,11,13,17]
BigSum = 0

for permut in AllComb:
    ii = 0
    while ii<7:
        if not l2int(permut[ii:3+ii]) % DivList[ii] == 0:
            break
        ii += 1
    if ii==7:
        BigSum += l2int(permut)

print(BigSum)
# 16695334890
