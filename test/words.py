test="3141592"
test2 = [x for x in test]
print(test2)

t="3141592"
p="271"

temp = []
plen = len(p)
tlen = len(t)
endindex = tlen - plen + 1

for i in range(0,endindex):
    temp.append(t[i:i+plen])


ans = filter(lambda x: x > p, temp)
print(list(ans))