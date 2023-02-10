import sys
sys.stdin = open("3079.txt")

n, m = map(int, input().split()) # n 검색대, m 검사할 사람

dic = {}
for _ in range(n):
    a = int(input())
    try:
        dic[a] +=1
    except:
        dic[a] = 1

# lst = []
# for _ in range(n):
#     lst.append(int(input()))

# 최대값은 최소시간 * 사람수로 정의
# 최소값은 0
end = min(dic.keys()) * m
start = 0

result = 0
while start <= end:
    people = 0
    mid = (start + end) // 2
    for num in dic:
        people += (mid // num) * dic[num]
    
    if people >= m:
        end = mid - 1  # mid는 이미 확인했으니 그보다 아래쪽으로 이동
        result = mid
    else:
        start = mid + 1
    

print(result)