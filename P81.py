"""
In the 5 by 5 matrix below, the minimal path sum from the
top left to the bottom right, by only moving to the right
and down, is indicated in bold red and is equal to 2427.


131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331

Find the minimal path sum, in matrix.txt (right click
and 'Save Link/Target As...'), a 31K text file containing
a 80 by 80 matrix, from the top left to the bottom right
by only moving right and down.
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

# S is a matrix of size M which will contain the cheapest cost to get
# to the finish from that square.
# eg [1 5; 2, 0] would give [3 5; 2 0]. As we can see from (0,0) cheapest
# is to travel through the 2 rather than the 5, thus 2+1 =3
S = np.zeros(np.shape(M), dtype='int32')


iio, jjo = np.shape(M)
ii = iio-1

while ii>=0:
    jj = jjo-1
    while jj>=0:
        print  ii, jj
        if (ii==iio-1) and (jj==jjo-1):
            S[ii,jj] = M[ii,jj]
        elif ii==iio-1:
            S[ii,jj] = M[ii,jj] + S[ii,jj+1]
        elif jj==jjo-1:
            S[ii,jj] = M[ii,jj] + S[ii+1,jj]
        else:
            S[ii,jj] = M[ii,jj] + min([S[ii+1,jj], S[ii,jj+1]])
        jj -= 1
    ii -= 1

print S[0,0]
#427337