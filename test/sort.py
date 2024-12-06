from itertools import combinations

# combinations(list, number)
## combinations(range(4), 3) --> (0,1,2), (0,1,3), (0,2,3), (1,2,3)
target = [1,2,3]
target_tuple = combinations(target, 3)
print(target_tuple)
target_tuple_list = list(combinations(target, 3))
print(target_tuple_list)