#==============================================================================
# By starting at the top of the triangle below and moving to adjacent numbers
# on the row below, the maximum total from top to bottom is 23.
# 
# 3
# 7 4
# 2 4 6
# 8 5 9 3
# 
# That is, 3 + 7 + 4 + 9 = 23.
# 
# Find the maximum total from top to bottom in triangle.txt (right click
# and 'Save Link/Target As...'), a 15K text file containing a triangle
# with one-hundred rows.
# 
# NOTE: This is a much more difficult version of Problem 18. It is not
# possible to try every route to solve this problem, as there are
# 299 altogether! If you could check one trillion (1012) routes every
# second it would take over twenty billion years to check them all.
# There is an efficient algorithm to solve it. ;o)
#==============================================================================


import numpy as np


#TrigRaw = '''3
#7 4
#2 4 6
#8 5 9 3'''


# Define function to import data files obtained from machine
def readfile(filename):
    # Open the file
    openfile = open(filename, 'rb')
#    for line in openfile:
#        print line[:-1].split(" ")
#        print 'next'
    # CSV reader, comma seperated, keeping second column only
    lines = [line[:-1].strip().split(" ") for line in openfile]
    Trig = []
    for line in lines:
        data = []
        for item in line:
            data.append(int(item))
        Trig.append(data)
    return Trig

TrigA = readfile('P67tri.txt')


length = len(TrigA)


TrigS = np.zeros([length,length])


ii, jj = 0, 0
for Vector in TrigA:
    jj = 00
    for Element in Vector:
#        print Element, ii, jj
        if ii==0:
            TrigS[ii][jj] = TrigA[ii][jj]
        elif jj==0:
            TrigS[ii][jj] = TrigA[ii][jj] + TrigS[ii-1][jj]
        else:
            TrigS[ii][jj] = TrigA[ii][jj] + max([TrigS[ii-1][jj-1], TrigS[ii-1][jj]])
        jj += 1
    ii += 1

#print TrigS[-1]
print max(TrigS[-1])
#7273