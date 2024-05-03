from functools import reduce
import copy
print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))

a = dict(a = 1,b = 2)
b = {"A":1, "b":2}
c = {'a':2, 'b':2}
print(a,b,c)

d = copy.deepcopy(a)
d['hello'] = "world"
print(d)
print(a)

print(id(d))
print(id(a))

f = d
print(id(f))
f["test"] = "test"
print(f)
print(d)

for key, value in d.items():
    print(f"key: {key}, value: {value}")