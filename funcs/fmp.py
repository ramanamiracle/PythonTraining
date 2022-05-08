l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(func, iterable): Return an iterator yielding those items of iterable for which func(item) is True

# map(func, iterable): Apply (or Map or Transform) the function func on each item of the iterable. For example

# for item in map(lambda x: x ** x, l):
#     print(item, end=' ')
#
# lst = [80, 85, 75, 85, 75]
#
# from functools import reduce
#
# print(reduce(lambda x, y: x * y, lst))

# Combining filter-map to produce a new sub-list
lst = [11, 22, 33, 44, 55]
new_lst = list(map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst)))
print(new_lst)

# Combining filter-map-reduce to obtain an aggregate value

from functools import reduce
print(reduce(lambda x, y: x+y, map(lambda x: x*x, filter(lambda x: x % 2 == 0, lst))))

