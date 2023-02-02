# n = int(input())
# lst = []

# for i in range(n):
#     lst.append(int(input()))

# lst.sort()

# max_power = 0
# for i in range(n):
#     if max_power < (lst[i:][0] * (n - i)):
#         max_power = lst[i:][0] * (n - i)

# print(max_power)

n = int(input())
lst = []
value = []

for i in range(n):
    lst.append(int(input()))

lst.sort()

max_power = 0
for i in range(n):
    value.append(lst[i] * (n-i))

print(max(value))