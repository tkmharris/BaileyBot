# allowable bid
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
	else:
	    return "Something's wrong!"

i = int(raw_input('bid 1\n'))
j = int(raw_input('bid 1\n'))
k = int(raw_input('bid 2\n'))
l = int(raw_input('bid 2\n'))

print allowed((i,j),(k,l))
