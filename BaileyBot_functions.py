import random
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
def counting(a,b):
	if b == 1:
	    return a.count(1)
	else:
	    return a.count(1) + a.count(b)

number = int(raw_input('How many dice?\n'))
count = int(raw_input('Count which number?\n'))

r = roll(number)
print r
print counting(r,count)

# Next: Write function to determine possible bids.
# Include method for determining lowest possible raises.

# Ideas: Different play styles? Cautious bids the least chance of being caught out. 
# Aggressive bids as close to 50% as possible.
# Include bluffs?
