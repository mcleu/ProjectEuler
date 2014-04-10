# -*- coding: utf-8 -*-
#==============================================================================
# Starting in the top left corner of a 2x2 grid, and only being able to move
#  to the right and down, there are exactly 6 routes to the bottom right corner.
#
# How many such routes are there through a 20x20 grid?
#==============================================================================

nsize = 20

import math

def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

def getPath(side):
    return nCr(2*side, side)

print getPath(nsize)
