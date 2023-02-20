import sys
sys.stdin = open("1874.txt")

n = int(input())
st = []  # 스택 
lst = []  # 나와야 할 리스트
comp_lst = []  # 비교할 리스트
anslst = []  # +- 저장할거
cnt = 0

for _ in range(n):
    lst.append(int(input()))

for i in range(1,n+1):
    st.append(i)
    anslst.append('+')
    while st and lst[cnt] == st[-1]:
        comp_lst.append(st.pop())
        anslst.append('-')
        cnt += 1

if st:
    print('NO')
else:
    for word in anslst:
        print(word)