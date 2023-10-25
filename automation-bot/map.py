target = [1,2,3,4,5]

def add(x):
    return x+1

result = map(add, target)
print(list(result))