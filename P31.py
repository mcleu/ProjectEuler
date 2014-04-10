"""
In England the currency is made up of pound, GBP, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, GBP1 (100p) and GBP2 (200p).
It is possible to make GBP2 in the following way:

1xGBP1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
How many different ways can GBP2 be made using any number of coins?
"""

Target = 200
counter = 0

for ii in range(Target, -1, -200):
    for jj in range(ii, -1, -100):
        for kk in range(jj, -1, -50):
            for ll in range(kk, -1, -20):
                for mm in range(ll, -1, -10):
                    for nn in range(mm, -1, -5):
                        for oo in range(nn, -1, -2):
                            counter += 1


print counter