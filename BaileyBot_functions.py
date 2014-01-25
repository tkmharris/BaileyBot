import random
import math
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
def counting(hand,number):
	if number == 1:
	    return hand.count(1)
	else:
	    return hand.count(1) + hand.count(number)

# possible totals.
def all_totals(m):
	return [(x,y) for x in range(1, m+1) for y in range(1,7)]


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
	
#IO stuff

#per = int(raw_input('How many dice?\n'))
tot = int(raw_input('How many dice in total?\n'))
#count = int(raw_input('Count which number?\n'))
i = int(raw_input('bid 1\n'))
j = int(raw_input('bid 2\n'))



offer = (i,j)
all_bids = all_totals(tot)
poss_bids = [tup for tup in all_bids if allowed(offer,tup)]

print poss_bids


# Include method for determining lowest possible raises.

# Ideas: Different play styles? Cautious bids the least chance of being caught out. 
# Aggressive bids as close to 50% as possible.
# Include bluffs?
