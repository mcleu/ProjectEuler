# -*- coding: utf-8 -*-
#==============================================================================
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
# containing over five-thousand first names, begin by sorting it into
# alphabetical order. Then working out the alphabetical value for each name,
# multiply this value by its alphabetical position in the list to obtain a
# name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
# COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?
#==============================================================================

import numpy as np

# Define function to import data files obtained from machine
def readfile(filename):
    # Open the file
    openfile = open(filename, 'rb')
#    for line in openfile:
#        print line[:-1].split(" ")
#        print 'next'
    names = openfile.next().split(",")
    outname = [name.strip('"') for name in names]
    outname.sort()
    return outname

Names = readfile('P022name.txt')

def GetPoints(Name):
    Name = Name.upper()
    Points = 0
    for letter in Name:
       Points += ord(letter)-64
    return Points

def TotalPoints(Names):
    ii = 1
    TP = 0
    for Name in Names:
        print Name, GetPoints(Name), ii, ii * GetPoints(Name)
        TP += ii * GetPoints(Name)
        ii += 1
    return TP

print TotalPoints(Names)
# 871198282