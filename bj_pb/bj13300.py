import sys
sys.stdin = open("input13300.txt")

n, k = map(int, input().split())

st_dict = {}
bang = 0

for i in range(2):  # 6학년까지 딕셔너리 생성
    for j in range(6):
        st_dict[(i, j+1)] = 0

for i in range(n):  # 성별, 학년 튜플로 받음
    st = tuple(map(int, input().split()))
    st_dict[st] += 1
    pass

for i in st_dict:  # 튜플로 키값 조회해 딕셔너리 값 증가
    if st_dict[i] % k == 0:
        bang += (st_dict[i] // k)
    else:
        bang += (st_dict[i] // k) + 1

print(bang)