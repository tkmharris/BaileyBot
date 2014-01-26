import random
import math
import probabilities

# This file keeps some of the basic functions for BaileyBot.

# Palifico yes no
def palifico(x):
	if x == 'n':
	    return False
	else:
	    return True

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

# Looks up probability on correct table depending on offer (need to add second table).
def offer_prob(tup, n):
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


# IO - currently takes total numeber of dice, number of own dice and offer
# and calculates probability of offer with own dice taken into account.
per = int(raw_input('How many dice do you have?\n'))
tot = int(raw_input('How many dice are there in total?\n'))
is_it_palifico = raw_input('Is it Palifico? (y/n)')

hand = roll(per)
i = int(raw_input("What's the offer: how many dice?\n"))
j = int(raw_input("What's the offer: which number on the dice?\n"))
offer = (i,j)
offer_mod_own = (i - counting(hand,j), j)
tot_mod_own = tot - per

all_bids = all_totals(tot)
poss_bids = [tup for tup in all_bids if allowed(offer,tup)]



print hand
print 'Probability of offer is', offer_prob(offer_mod_own, tot_mod_own),"%."



# Include method for determining lowest possible raises.
# Idea: Add lines from Alex's thesis/papers for BaileyBot to say at random.
# Ideas: Different play styles? Cautious bids the offer with least chance of being caught out. 
# Aggressive bids as close to 50% as possible.
# Include bluffs?
