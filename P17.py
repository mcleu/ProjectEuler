# -*- coding: utf-8 -*-
#==============================================================================
# If the numbers 1 to 5 are written out in words: one, two, three, four,
# five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were
# written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred
# and forty-two) contains 23 letters and 115 (one hundred and fifteen)
# contains 20 letters. The use of "and" when writing out numbers is
# in compliance with British usage.
#==============================================================================




single = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
          'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
          'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
        'eighty', 'ninety']



def spellnum(num):
    '''
    Returns the spelled out version of the number
    '''
    num = int(num)
    written = ''
    # Do the thousands
    if num >= 1000:
        ntho = num//1000
        written += single[ntho] + ' thousand'
        num = num - 1000*ntho

    # Do the hundreds
    if num >= 100:
        nhun = num//100
        written += single[nhun] + ' hundred'
        num = num - 100*nhun

    if not (num == 0):
        if not (written == ''):
            written += ' and'
        # Do the tens
        if num >= 20:
            nten = num//10
            written += ' ' + tens[nten]
            num = num - 10*nten

        # Add the single digits
        written += ' ' + single[num]
    return written.lstrip()

def letcnt(string):
    return len( "".join(string.split()) )

tlen = 0
for ii in xrange(1, 1001):
#    print spellnum(ii)
    tlen += letcnt(spellnum(ii))

print tlen