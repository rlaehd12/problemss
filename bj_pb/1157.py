a = input()
a = a.upper()
b = set(a)
b = list(b)
count = [0] * len(b)
for word in a:
    count[b.index(word)] += 1


l = count.index(max(count))
r = count[::-1].index(max(count))

if l != len(count) - 1 - r:
    print('?')
else:
    print(b[l])