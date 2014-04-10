# -*- coding: utf-8 -*-
#==============================================================================
# The nth term of the sequence of triangle numbers is given by,
# tn = 0.5 n(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding
# to its alphabetical position and adding these values we form
# a word value. For example, the word value for SKY is
# 19 + 11 + 25 = 55 = t10. If the word value is a triangle
# number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'),
# a 16K text file containing nearly two-thousand common
# English words, how many are triangle words?
#==============================================================================


# Define function to import data files obtained from machine
def readfile(filename):
    openfile = open(filename, 'rb')
    names = openfile.next().split(",")
    outname = [name.strip('"') for name in names]
    return outname

words = readfile('P042words.txt')

def GetPoints(Word):
    Word = Word.upper()
    Points = 0
    for letter in Word:
       Points += ord(letter)-64
    return Points

mpts = 0 # Maximim number of points
ptslist = []
for word in words:
    pts = GetPoints(word)
    ptslist.append(pts)
    mpts = pts if (pts>mpts) else mpts


Tri = lambda n : int(0.5*n*(n+1))

Tlist = []
n = 1
Tnext = 0

while Tnext<mpts:
    Tnext = Tri(n)
    Tlist.append(Tnext)
    n += 1

cnt = 0

for pts in ptslist:
    try:
        Tlist.index(pts)
        cnt += 1
    except:
        pass

print cnt
# 162