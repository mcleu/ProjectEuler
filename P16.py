# -*- coding: utf-8 -*-
#===============================================================================
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?
#===============================================================================

x = 2**1000
s = str(x)
sod = 0
print x
for i in s:
    sod += int(i)


print sod
