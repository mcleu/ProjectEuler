#===============================================================================
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the 
# numbers from 1 to 20?
#===============================================================================

def find10():
#    n = 2520
    n=20
    while (1):
#        print n
        for nn in [9,8,7]: # Tests number 1, ..., 9
#            print 'testing with ' + str(nn)
            if n%nn==0:
                if nn==7:
                    return n
                continue
            break
        n += 20 # Take multiples of 20 (This covers 1,2,5,10)


def find20():
#    n = 232792560
    n=220
    while (1):
#        print n
        for nn in [19,18,17,16,15,14,13]: # Tests number 11, ..., 19
#            print 'testing with ' + str(nn)
            if n%nn==0:
                if nn==13:
                    return n
                continue
            break
        n += 220 # Take multiples of 20 (This covers 1,2,5,10,11)

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in xrange(n)]
    else:
        starttime = time.clock()
        times=[]
        while (time.clock()-starttime)<n:
            times.append( timedcall(fn, *args)[0] )
    return min(times), average(times), max(times)

print find20()
print timedcalls(10.0, find20)
