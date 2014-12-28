# -*- coding: utf-8 -*-
#==============================================================================
# A googol (10**100) is a massive number: one followed by one-hundred zeros;
# 100**100 is almost unimaginably large: one followed by two-hundred zeros.
# Despite their size, the sum of the digits in each number is only 1.
# 
# Considering natural numbers of the form, ab, where a, b < 100,
# what is the maximum digital sum?
#==============================================================================

def strsum(numstr):
    numsum = 0
    for digit in numstr:
        numsum += int(digit)
    return numsum


maxsum = 0
for a in range(101):
    for b in range(101):
        thesum = strsum(str(a**b))
        if (maxsum < thesum):
            maxsum = thesum

print maxsum # 972
