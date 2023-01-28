import sys
sys.stdin = open('input2564.txt')
# 동근 위치 1
def north(lst, loc): # loc는 donguen[1] 하나만 받을거임
    sums = 0
    for market in lst:
        if market[0] == 3:
            sums += loc + market[1]
        elif market[0] == 4:
            sums += row - loc + market[1]
        elif market[0] == 1:
            sums += abs(loc - market[1])
        else:
            sums += min(loc + col + market[1], 2 * row - loc - market[1] + col)
    return sums

# pos 2
def south(lst, loc): # loc는 donguen[1] 하나만 받을거임
    sums = 0
    for market in lst:
        if market[0] == 3:
            sums += loc + col - market[1]
            #print(sums)
        elif market[0] == 4:
            sums += row - loc + col - market[1]
            #print(sums)
        elif market[0] == 2:
            sums += abs(loc - market[1])
            #print(sums)
        else:
            sums += min(loc + col + market[1], 2 * row - loc - market[1] + col)
            #print(sums)
    return sums
# pos 3
def west(lst, loc): # loc는 donguen[1] 하나만 받을거임
    sums = 0
    for market in lst:
        if market[0] == 1:
            sums += loc + market[1]
        elif market[0] == 2:
            sums += col - loc + market[1]
        elif market[0] == 3:
            sums += abs(loc - market[1])
        else:
            sums += min(loc + row + market[1], 2 * col - loc - market[1] + row)
    return sums

# pos 4
def east(lst, loc): # loc는 donguen[1] 하나만 받을거임
    sums = 0
    for market in lst:
        if market[0] == 1:
            sums += loc + row - market[1]
        elif market[0] == 2:
            sums += col - loc + row - market[1]
        elif market[0] == 4:
            sums += abs(loc - market[1])
        else:
            sums += min(loc + row + market[1], 2 * col - loc - market[1] + row)
    return sums


lst = []

row, col = map(int, input().split())
n = int(input())

for i in range(n):
    lst.append(tuple(map(int, input().split())))

donguen = tuple(map(int, input().split()))

# print(lst)
# print(donguen)

if donguen[0] == 1:
    print(north(lst, donguen[1]))
elif donguen[0] == 2:
    print(south(lst, donguen[1]))
elif donguen[0] == 3:
    print(west(lst, donguen[1]))
else:
    print(east(lst, donguen[1]))