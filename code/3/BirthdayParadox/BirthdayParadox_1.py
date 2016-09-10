from collections import Counter

lst = [1, 2, 3, 5, 1]
lst2 = [1, 2, 3, 4, 5]
lst3 = []


def has_duplicate(lst):
    collectlst = Counter(lst)
    for i in collectlst:
        if collectlst[i] > 1:
            return True
        else:
            return False
    return False


print has_duplicate(lst)
print has_duplicate(lst2)
print has_duplicate(lst3)
