# -*- coding: utf-8 -*-
"""
Consider the fraction, n/d, where n and d are positive integers.
 If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in
ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7,
1/3, 3/8, 2/5, 3/7, 1/2,
4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the
sorted set of reduced proper fractions for d ≤ 12,000?
"""

# Source: Wikipedia
def farey(n):
    """Python function to print the nth Farey sequence."""
    a, b, c, d = 0, 1,  1 , n     # (*)
    yield (a,b)
    while (c <= n):
        k = int((n + b)/d)
        a, b, c, d = c, d, k*c - a, k*d - b
        yield (a,b)


def nBetween(d, lower, upper):
    count = 0
    nGen = farey(d)
    while True:
        try:
            ntotest = nGen.next()
            if (float(ntotest[0])/ntotest[1]) > lower:
                if (float(ntotest[0])/ntotest[1]) >= upper:
                    break
                count += 1
        except StopIteration:
            break
    return count

nfactors = nBetween(12000, 1.0/3, 1.0/2)
print nfactors #7295372
