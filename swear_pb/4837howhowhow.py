import sys
sys.stdin = open("4837.txt")

# t = int(input())

# for test_case in range(1, t+1):
#     n, t = map(int, input().split())  #n = 부분집합개수, t는 목표값
#     my_lst = [(i+1) for i in range(12)]  # 1~12 리스트

#     ans = 0
#     for i in range(1<<12):  # 2^12개 다 확인
#         cnt = 0  # 1이 몇개인지 확인용
#         subset_lst = []  # 부분집합 리스트 초기화
#         for j in range(12):  # 각 자리 전부 확인용
#             if i & (1<<j):
#                 cnt += 1
#                 subset_lst.append(my_lst[j])
#         if cnt == n:  # 다 돌아서 1이 n개면
#             if sum(subset_lst) == t:  # 그 부분집합 t와 같은지 확인
#                 ans += 1  #같으면 +1
    
#     print(f'#{test_case} {ans}')

def cases(array, n):
    result = []
    if n == 0:
        return [[]]
    for i in range(len(array)):
        element = array[i]
        for rest in cases(array[i + 1:], n-1):
            result.append([element] + rest)
    return result
 
test_case = int(input())
test_cnt = 1
A_list = [x for x in range(1,13)]
 
for _ in range(test_case):
    A, K = map(int, input().split())
    answer = 0
    possible_A = cases(A_list, A)
    for case in possible_A:
        if sum(case) == K:
            answer += 1
    print(f'#{test_cnt} {answer}')
    test_cnt += 1