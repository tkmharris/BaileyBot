import random

def dice():
	return random.randint(1,6)

def roll(n):
	if n < 1:
	    print "positive integers only please"
	l = []
	for i in range(1,n+1):
	    l = l + [dice()]
	return l

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


