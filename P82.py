"""
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, by starting
in any cell in the left column and finishing in any cell in
the right column, and only moving up, down, and right, is
indicated in red and bold; the sum is equal to 994.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click and
'Save Link/Target As...'), a 31K text file containing a
80 by 80 matrix, from the left column to the right column.
"""

import numpy as np

# Define function to import data files obtained from machine
def readfile(filename):
    # Open the file
    openfile = open(filename, 'rb')
    # CSV reader, comma seperated, keeping second column only
    lines = [line.strip().split(",") for line in openfile]
    Trig = []
    for line in lines:
        data = []
        for item in line:
            data.append(int(item))
        Trig.append(data)
    return Trig

Matrix = readfile('P81matrix.txt')
M = np.array(Matrix)

# S is a 2D array of size M which will contain the cheapest cost to get
# to the finish from that square.
# eg [1 5; 2, 0] would give [3 5; 2 0]. As we can see from (0,0) cheapest
# is to travel through the 2 rather than the 5, thus 2+1 =3
S = np.zeros(np.shape(M), dtype='int32')
S[:,79] = M[:,79]

iio, jjo = np.shape(M)
jj = jjo-2

while jj>=0:
    # Neex to keep looping until not changing anymore
    # So is S vector in previous run
    So = np.copy(S[:,jj])
    # First pass is copy over S and add self
#    print 'prior', So
    S[:,jj] = S[:,jj+1] + M[:,jj]
#    print 'after', So
#    print S[:,jj], So, S[:,jj]==So
    while not (S[:,jj]==So).all():
        So = np.copy(S[:,jj])
        ii = iio-1
        while ii>=0:
#            print  ii, jj
            if (ii==iio-1):
                S[ii,jj] = M[ii,jj] + min([S[ii,jj+1], S[ii-1,jj]])
            elif ii==0:
                S[ii,jj] = M[ii,jj] + min([S[ii,jj+1], S[ii+1,jj]])
            else:
                S[ii,jj] = M[ii,jj] + min([S[ii,jj+1], S[ii-1,jj], S[ii+1,jj]])
            ii -= 1
#        print S[:,jj], So, S[:,jj]==So
    jj -= 1


print S[:,0]
print min(S[:,0])
#349326