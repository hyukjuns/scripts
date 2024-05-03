test = [[1,2],[3,4]]
val =  max(max(x) for x in test) * max(min(x) for x in test)
print(val)

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(), w.lower(), len(w)] for w in words]
for i in stuff:
    print(i)

print()
stuff = map(lambda w: [w.upper(), w.lower(), len(w)], words)
for i in stuff:
    print(i)