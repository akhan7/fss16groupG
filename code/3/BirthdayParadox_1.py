from collections import Counter

lst = [1, 2, 3, 5, 1]

def has_duplicate(lst):
	collectlst = Counter(lst) 
	for i in collectlst:
		if collectlst[i] > 1:
			print 'Duplicate items found'
			return True
		else:
			print 'Duplicate items not found'
			return False
has_duplicate(lst)

