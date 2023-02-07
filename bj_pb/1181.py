import sys
sys.stdin = open("1181.txt")

t = int(input())

lst = []
for i in range(t):
    lst.append(input())
lst = set(lst)
lst = list(lst)
lst.sort()

len_lst = []

for i in lst:
    len_lst.append(len(i))

length = set(len_lst)
length = list(length)
length.sort()
new_lst = []

for i in length:
    for word in range(len(lst)):
        if len_lst[word] == i:
            new_lst.append(lst[word])

for i in new_lst:
    print(i)