import sys
sys.stdin = open("input1945.txt")

t = int(input())

# for tc in range(t): # 2, 3, 5, 7, 11
#     number = int(input())
#     lst = [0] * 5
#     while not (number % 2):  # 0은 false
#         number //= 2
#         lst[0] += 1
    
#     while not (number % 3):  # 0은 false
#         number //= 3
#         lst[1] += 1
    
#     while not (number % 5):  # 0은 false
#         number //= 5
#         lst[2] += 1
    
#     while not (number % 7):  # 0은 false
#         number //= 7
#         lst[3] += 1
    
#     while not (number % 11):  # 0은 false
#         number //= 11
#         lst[4] += 1
    
#     #print(lst)

#     print(f'#{tc + 1}', end= ' ')
#     for j in lst:
#         print(j, end=' ')
#     print('')
    

#     pass

#### 교수님 풀이
divs = [2, 3, 5, 7, 11]

for test_case in range(1, t + 1): # 2, 3, 5, 7, 11
    N = int(input())
    cnts = [0] * len(divs)

    for i in range(len(divs)):
        while N % divs[i] == 0:
            cnts[i] += 1
            N = N//divs[i]

    print(f'#{test_case}', *cnts)