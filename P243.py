# -*- coding: utf-8 -*-
#==============================================================================
# A positive fraction whose numerator is less than its
# denominator is called a proper fraction.
# For any denominator, d, there will be d-1 proper
# fractions, for example with d = 12:
# 1/12, 2/12, 3/12, 4/12, 5/12, 6/12, 7/12,
# 8/12, 9/12, 10/12, 11/12.
#
# We shall call a fraction that cannot be cancelled
# down a resilient fraction.
# Furthermore we shall define the resilience of a
# denominator, R(d), to be the ratio of its proper
# fractions that are resilient; for example,
# R(12) = 4/11 .
# In fact, d = 12 is the smallest denominator
# having a resilience R(d) < 4/10.
#
# Find the smallest denominator d, having a
# resilience R(d) < 15499/94744 .
#==============================================================================


def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return (a * b) // gcd(a, b)