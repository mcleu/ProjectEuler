# -*- coding: utf-8 -*-
#==============================================================================
# An irrational decimal fraction is created by concatenating the positive
# integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the
# value of the following expression.
#
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
#==============================================================================

# Solve using logic

# 1-9 corresponds to digits 1-9 (9*1)
# 10-99 corresponds to digits 10-189 (90*2)
# 100-999 corresponds to digits 190-2889 (900*3)
# 1000-9999 corresponds to digits 2890-38889 (9k*4)
# 10k-99k corresponds to digits 38890-488889 (90k*5)
# 100k-999k corresponds to digits 488890-5888889 (900k*6)
# etc

# Finding what it corresponds to. Eg d55. First as its in d10-189,
# we know the number is between 10-99. Next, we subtract by the d_start,
# or 10, and divide by 2 (len of digits).
# 45/2=22. So it is in the string 22+10= "32"
# Next 45%2 is 1, so it is the 2nd digit
# (0 would be the 3 of 32, 1 is the 2) remember use python indexing

# d_100 --> Number between 10-99
# (100 - 10)/2 = 45
# number is 45 + 10 = 55
# 45 % 2 = 1,         0^
# Hence, d_100 = 5

# d_1M --> Number between 100k-999k
# (1M - 488890)/6 = 85185
# number is 85185 +100k = 185 185
# 85185 % 6 = 3,          012 ^45
# Hence, d_1M = 1

# d_1 = 1
# d_10 = 1
# d_100 = 5
# d_1k = 3
# d_10k = 7
# d_100k = 2
# d_1M = 1

# 5*3*7*2 = 210


#==============================================================================
# Slow solution, as need to create string of >1M characters
#==============================================================================

#nums=''
#
#for i in range(1200000):
#    # Note I include the 0 in range so index 0 is 0 to correct the index
#    nums = nums + str(i)
#
#print int(nums[1])*int(nums[10])*int(nums[100])*int(nums[1000])*int(nums[10000])*int(nums[100000])*int(nums[1000000])
