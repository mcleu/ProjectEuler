# -*- coding: utf-8 -*-
#==============================================================================
# The fraction 49/98 is a curious fraction, as an inexperienced mathematician
# in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator
# and denominator.
#
# If the product of these four fractions is given in its lowest common
# terms, find the value of the denominator.
#==============================================================================


for denom in xrange(10,100):
    for numer in xrange(10,denom):
        if str(numer)[1:2]==str(denom)[0:1]:
            #print numer, denom,
            try:
                simple = int(numer/10) / float(denom%10)
            except:
                simple = 0
            if float(numer)/denom == simple:
                print numer, denom
# 16 64
# 26 65
# 19 95
# 49 98

# 1/4 * 2/5 * 1/5 * 1/2 = 1/100
