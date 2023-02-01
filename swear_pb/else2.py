import sys
sys.stdin = open('input11.txt')

def check(lista):
    if lista[0] == 'erase':
        print('a')
    elif lista[0] == 'add':
        print(lista[1])
    elif lista[0] == 'move':
        print(lista[1])

T = int(input())

for i in range(T):
    order = input().split()
    check(order)