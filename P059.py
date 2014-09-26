# -*- coding: utf-8 -*-
#==============================================================================
# Each character on a computer is assigned a unique code and the preferred
# standard is ASCII (American Standard Code for Information Interchange).
# For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
#
# A modern encryption method is to take a text file, convert the bytes to
# ASCII, then XOR each byte with a given value, taken from a secret key.
# The advantage with the XOR function is that using the same encryption key
# on the cipher text, restores the plain text; for example, 65 XOR 42 = 107,
# then 107 XOR 42 = 65.
#
# For unbreakable encryption, the key is the same length as the plain text
# message, and the key is made up of random bytes. The user would keep the
# encrypted message and the encryption key in different locations, and
# without both "halves", it is impossible to decrypt the message.
#
# Unfortunately, this method is impractical for most users, so the modified
# method is to use a password as a key. If the password is shorter than the
# message, which is likely, the key is repeated cyclically throughout the
# message. The balance for this method is using a sufficiently long
# password key for security, but short enough to be memorable.
#
# Your task has been made easy, as the encryption key consists of three
# lower case characters. Using cipher.txt (right click and
# 'Save Link/Target As...'), a file containing the encrypted ASCII codes,
# and the knowledge that the plain text must contain common English words,
# decrypt the message and find the sum of the ASCII values in the
# original text.
#==============================================================================

# P059_cipher.txt

from itertools import permutations
import copy


def decodearray(array, key):
    keylen = len(key)
    stdout = copy.deepcopy(array)
    for ii in range(len(array)):
        stdout[ii] = array[ii] ^ key[ii%keylen]
    return stdout

def readfile(filename):
    # Open the file
    openfile = open(filename, 'rb')
    text = openfile.next().split(",")
    numbers = [int(txt) for txt in text]
    return numbers

def concat(array):
    strout = ''
    for char in array:
        strout = strout + char
    return strout

cipher = readfile('P059_cipher.txt')
#cipher = readfile('P059_ciphershort.txt')

list_of_keys = permutations(range(97,123),3)
# return aaa aab aac ... zzy zzz

for key in list_of_keys:
    numkey = key
    message = decodearray(cipher, key)
    msg_str = concat( [chr(m) for m in message] )
    if ' the ' in msg_str: 
        print msg_str
        print sum([ord(i) for i in msg_str])
