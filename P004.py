# -*- coding: utf-8 -*-
#===============================================================================
# A palindromic number reads the same both ways. The largest palindrome made
# from the product of two 2-digit numbers is 9009 = 91 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
#===============================================================================

def isPalindrome(n):
    s=str(n)
    return s==s[::-1]

m=0
for ii in range(999,800,-1):
    for jj in range(999,800,-1):
        nums = ii*jj
        if isPalindrome(nums):
            m=max(m,nums)
            print ii,jj,nums
            
print 'largest palindrome is', m