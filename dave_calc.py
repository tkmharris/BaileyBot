import itertools

def small_list(i):
	return [(i,x) for x in range(1,i+1)]

n = int(raw_input('What is n?\n'))

count=2

functions = small_list(1)
while count <= n:
	functions = list(itertools.product(functions,small_list(count)))
	count = count + 1

print functions


