import random
import math
import probabilities
import operator

# palifico or not
is_it_palifico = raw_input('Is it Palifico? (y/n)')
# Palifico yes no
def palifico(x):
	if x == 'n':
	    return False
	else:
	    return True

# This file keeps some of the basic functions for BaileyBot.

# Rolls a die.
def dice():
	return random.randint(1,6)

# Rolls n dice.
def roll(n):
	if n < 1:
	    print "positive integers only please"
	else:
	    return [dice() for i in range(1, n+1)]

# Counts the number of aces or other numbers.
# a is input set, b is number to be counted.
def counting(h,number):
	if number == 1 or palifico(is_it_palifico):
	    return h.count(number)
	else:
	    return h.count(1) + h.count(number)

# counts the number of each value we have (adjusted for ones)
def my_totals(h):
	return {number:counting(h,number) for number in range(1,7)}

# returns the value we have the most of (adjusted for ones)
def most(h):
	return max((my_totals(h)).iteritems(), key=operator.itemgetter(1))[0]

# returns the bid once own hand is taken into account
def bid_mod_own(i,j, hand):
	return (i - counting(hand,j), j)

# possible totals.
def all_totals(m):
	if palifico(is_it_palifico):
	    return [(x,y) for x in range(1, min(m+1,11)) for y in range(1,7)]
	else: 
	    return [(x,1) for x in range(1, min(m+1,11))] + [(x,y) for x in range(1, min(m+1,16)) for y in range(2,7)]



# allowable raises
# input (0,0) as bid to allow all bids, i.e. starting bid.
def allowed(tup1, tup2):
	if tup1[1]==1:
	    if (tup2[1]==1 and tup2[0] > tup1[0]) or (tup2[0] > 2*tup1[0]):
	        return True
	    else:
	        return False
	elif tup1[1]!=1:
	    if (tup2[0]>tup1[0]) or (tup2[1]==1 and tup2[0]>int((tup1[0]-1)/2.0)) or (tup2[0]==tup1[0] and tup2[1]>tup1[1]):
	        return True
	    else:
	        return False
	elif tup1 == (0,0):
	    return True
	else:
	    return "Something's wrong!"

# Looks up probability on correct table depending on tuple (need to add second table).
def tup_prob(tup, n):
	if tup[1] == 1 or palifico(is_it_palifico):
	    if tup[0] > 10:
	        return 0
	    elif tup[0] < 1:
	        return 100	        
	    else:
		return probabilities.ace(tup[0],n)
	else:	    
	    if tup[0] > 15:
	        return 0	        
	    elif tup[0] < 1:
	        return 100
	    else:
		return probabilities.non_ace(tup[0],n)	    

# looks up probability on correct table of tuple modified for own hand
def tup_prob_mod(tup, n, h):
	return tup_prob(bid_mod_own(tup[0],tup[1],h),n)



