import sys
sys.stdin = open("input1931.txt")

n = int(input())

room = []

for i in range(n):
    room.append(list(map(int, input().split())))

room.sort(key = lambda x: x[0])
room.sort(key = lambda x: x[1])

count = 1
cur_room = room[0]

for i in range(n):
    if cur_room[1] <= room[i][0]:
        cur_room = room[i]
        count += 1

print(count)