# -*- coding: utf-8 -*-
#==============================================================================
# Comparing two numbers written in index form like 211 and 37 is not difficult,
# as any calculator would confirm that 211 = 2048 < 37 = 2187.
# 
# However, confirming that 632382**518061 > 519432**525806
# would be much more difficult, as both numbers contain over
# three million digits.
# 
# Using base_exp.txt (right click and 'Save Link/Target As...'),
# a 22K text file containing one thousand lines with a base/exponent pair
# on each line, determine which line number has the greatest numerical value.
# 
# NOTE: The first two lines in the file represent the numbers in
# the example given above.
#==============================================================================

import numpy as np

# Define function to import data files obtained from machine
def readfile(filename):
    openfile = open(filename, 'rb')
    output = []
    for line in openfile:
        pair = line.split(",")
        output.append([int(pair[0]), int(pair[1])])
    return np.array(output)


num = readfile('P099_base_exp.txt')

# We can find the larger number by using the formula log(x**y) = y * log(x)
def isLarger(a,b):
    return (num[a,1]*np.log(num[a,0])) > (num[b,1]*np.log(num[b,0]))

A = 1
B = 2

for ii in range(2,len(num)):
    if isLarger(A,B):
        B = ii
    else:
        A = ii

if isLarger(A,B):
    print A + 1 # I add 1 because python indexes from 0
else:
    print B + 1

# 709
