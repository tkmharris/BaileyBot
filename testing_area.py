
is_it_palifico = 'y'


# Palifico yes no
def palifico(x):
	if x == 'n':
	    return False
	else:
	    return True

# possible totals.
def all_totals(m):
	if palifico(is_it_palifico):
	    return [(x,y) for x in range(1, min(m+1,11)) for y in range(1,7)]
	else: 
	    return [(x,1) for x in range(1, min(m+1,11))] + [(x,y) for x in range(1, min(m+1,16)) for y in range(2,7)]


