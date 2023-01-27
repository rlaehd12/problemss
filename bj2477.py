import sys
sys.stdin = open('input2477.txt')

T = int(input()) # 마지막에 곱할거
my_list = []

for i in range(6):

    m, n = map(int, input().split())
    my_list.append(n)

#print(my_list)
biggest_area = 0

for i in range(6):
    if biggest_area < my_list[i] * my_list[i-1]:
        biggest_area = my_list[i] * my_list[i-1]
        a = i-1

#print(biggest_area)
#print(a)

b = my_list[a-2] * my_list[a-3]
biggest_area -= b
#print(biggest_area)

print(biggest_area * T)