#!/usr/bin/python

# BaileyBot, the Perudo playing Alex Bailey replacement. Sometimes also known as The Alex Automaton.

import random, math, prob, operator

########################################
##  Some of the basic functions for BaileyBot.
##
########################################

# Rolls n dice.
def roll(n): return [random.randint(1,6) for i in range(n)]

# Counts the number of aces or other numbers.
# a is input set, b is number to be counted.
def counting(h,n):
	if n == 1 or palifico:
	    return h.count(n)
	else:
	    return h.count(1) + h.count(n)

# counts the number of each value we have (adjusted for ones)
def totals(h):
	return {n:counting(h,n) for n in range(1,7)}

# returns the value we have the most of (adjusted for ones)
def most(h):
	return max((totals(h)).iteritems(), key=operator.itemgetter(1))[0]

# returns the bid once own hand is taken into account
def bid_mod_own(i,j, hand):
	return (i - counting(hand,j), j)

# possible totals.
def all_totals(m):
	if palifico:
	    return [(x,y) for x in range(1, min(m+1,11)) for y in range(1,7)]
	else: 
	    return [(x,1) for x in range(1, min(m+1,11))] + \
                   [(x,y) for x in range(1, min(m+1,16)) for y in range(2,7)]

# allowable raises
# input (0,0) as bid to allow all bids, i.e. starting bid.
def allowed(tup1, tup2):
	if palifico:
	    if tup2[1]==tup1[1] and tup2[0] > tup1[0]:
	        return True
	    else:
	        return False
	elif tup1[1]==1:
	    if (tup2[1]==1 and tup2[0] > tup1[0]) or (tup2[0] > 2*tup1[0]):
	        return True
	    else:
	        return False
	elif tup1[1]!=1:
	    if (tup2[0]>tup1[0]) or (tup2[1]==1 and tup2[0]>int((tup1[0]-1)/2.0)) \
                                 or (tup2[0]==tup1[0] and tup2[1]>tup1[1]):
	        return True
	    else:
	        return False
	elif tup1 == (0,0):
	    return True
	else:
	    return "Something's wrong!"

# Looks up probability on correct table depending on tuple (need to add second table).
def tup_prob(tup, n):
	if tup[1] == 1 or palifico:
	    if tup[0] > 10:
	        return 0
	    elif tup[0] < 1:
	        return 100	        
	    else:
		return prob.ace(tup[0],n)
	else:	    
	    if tup[0] > 15:
	        return 0	        
	    elif tup[0] < 1:
	        return 100
	    else:
		return prob.non_ace(tup[0],n)	    

# looks up probability on correct table of tuple modified for own hand
def tup_prob_mod(tup, n, h):
	return tup_prob(bid_mod_own(tup[0],tup[1],h),n)

#########################
##  INPUT VALIDATION
##
#########################

def yesNoInput(question):
	while True:
		raw = raw_input(question + ' (y/n)')
		if raw.lower().strip() == 'y':
			return True
		elif raw.lower().strip() == 'n':
			return False
		else:
			print "Invalid input, enter \'y\' or \'n\'"

def integerInput(question, lowerBound, upperBound):
	while True:
		raw = raw_input(question)
		try:
			val = int(raw)
		except ValueError:
			print "Invalid Input"
			continue
		if val <= upperBound and val >= lowerBound:
			return val
		else:
			print "Invalid Input"
	

##########################
## MAIN
## 
##########################

if __name__=="__main__":

        # palifico or not
        palifico = yesNoInput('Is it Palifico?')

        #initial setup, numbers of dice. BaileyBot rolls.
        per = integerInput('How many dice do you have? (1-5)', 1,5)
        tot = integerInput('How many dice are there in total? (' + str(per+1) + '-?)', per+ 1, 100)  #TODO
        hand = roll(per)
        tot_mod_own = tot - per
        all_bids = all_totals(tot)

        # should it start?
        start = yesNoInput('Should I start?')

        # possible starting bids
        poss_start_bids = [(tup, tup_prob_mod(tup, tot_mod_own, hand)) for tup in all_bids \
                           if  tup_prob_mod(tup, tot_mod_own, hand) > 75 and tup[1] != 1]
        another = True

        if start: print random.choice(poss_start_bids)[0]

        while not yesNoInput('Should I reveal?'):
                i = integerInput("What's the offer: how many dice?", 1, 20)
                j = integerInput("What's the offer: which number on the dice?", 1, 6)
                offer = (i,j)
                offer_prob = tup_prob_mod((i,j), tot_mod_own, hand)
                poss_bids = [(tup, tup_prob_mod(tup, tot_mod_own, hand)) for tup in all_bids \
                            if allowed(offer,tup) and tup_prob_mod(tup, tot_mod_own, hand) > (100-offer_prob)]
                
                if poss_bids == [] or j>6:
                    print "Dudo!"
                    break
                else:
                    best_bid = max((dict(poss_bids)).iteritems(), key=operator.itemgetter(1))[0]
                    viable_bids = [(k,v) for k, v in (dict(poss_bids)).iteritems()  \
                                         if v > (tup_prob_mod(best_bid, tot_mod_own, hand)-10)]
                    print random.choice(viable_bids)[0]

        print hand


