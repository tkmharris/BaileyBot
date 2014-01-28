# Counts the number of aces or other numbers.
import random
import math
import probabilities
import operator
import BaileyBot_functions

#initial setup, numbers of dice. BaileyBot rolls.
per = int(raw_input('How many dice do you have?\n'))
tot = int(raw_input('How many dice are there in total?\n'))
hand = BaileyBot_functions.roll(per)

# palifico or not
is_it_palifico = raw_input('Is it Palifico? (y/n)')
tot_mod_own = tot - per
all_bids = BaileyBot_functions.all_totals(tot)

# should it start?
start = raw_input('Should I start? (y/n)')

# possible starting bids
poss_start_bids = [(tup, BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand)) for tup in all_bids if allowed(offer,tup) and BaileyBot_functions.tup_prob_mod(tup, tot_mod_own, hand)> 90]

if start == 'y':
	print poss_start_bids

print "hi"







