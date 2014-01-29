import random
from random import choice
import math
import probabilities
import operator
import BaileyBot_functions

print random.randint(1,6)

#initial setup, numbers of dice. BaileyBot rolls.
per = int(raw_input('How many dice do you have?\n'))
tot = int(raw_input('How many dice are there in total?\n'))
hand = BaileyBot_functions.roll(per)
tot_mod_own = tot - per
all_bids = BaileyBot_functions.all_totals(tot)



# should it start?
start = raw_input('Should I start? (y/n)')

# possible starting bids
poss_start_bids = [(tup, BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand)) for tup in all_bids if  BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand) > 75 and tup[1] != 1]
another = 'y'

if start == 'y':
	print poss_start_bids
	print choice(poss_start_bids)[0]

reveal = raw_input('Should I reveal? (y/n)')
if reveal == 'y':
	another = 'n'


while another == 'y':
	i = int(raw_input("What's the offer: how many dice?\n"))
	j = int(raw_input("What's the offer: which number on the dice?\n"))
	offer = (i,j)	
	offer_prob = BaileyBot_functions.tup_prob_mod((i,j), tot_mod_own, hand)
	poss_bids = [(tup, BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand)) for tup in all_bids if 			  BaileyBot_functions.allowed(offer,tup) and BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand) > (100-offer_prob)]
	
	if poss_bids == [] or j>6:
	    print "Dudo!"
	    another = 'n'

	else:
	    best_bid = max((dict(poss_bids)).iteritems(), key=operator.itemgetter(1))[0]
	    viable_bids = [(k,v) for k, v in (dict(poss_bids)).iteritems() if v > (BaileyBot_functions.tup_prob_mod(best_bid, tot_mod_own, hand)-10)]
	    print "Probabiliy of offer is",offer_prob
	    print choice(viable_bids)[0]
	    another = raw_input("Another_offer? (y/n)")

print hand

# Include method for determining lowest possible raises.
# Idea: Add lines from Alex's thesis/papers for BaileyBot to say at random.
# Ideas: Different play styles? Cautious bids the offer with least chance of being caught out. 
# Aggressive bids as close to 50% as possible.
# Include bluffs?
