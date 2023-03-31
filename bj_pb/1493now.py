length, width, height = map(int, input().split())
N = int(input())
boxes = [0] * 21  # 내가 가진 박스
for _ in range(N):
    a, b = map(int, input().split())
    boxes[a] = b
# print(boxes)
# 부피 확인
V = length*width*height
boxv = 0  
ans = 0
before = 0
cur = 0
# 가장 큰 박스부터 넣었다가 빼보면서 확인
for i in range(20,-1,-1):
    if boxes[i]:  # 2^i크기의 박스가 있으면
        cn = 2**i
        cur = (length//cn)*(width//cn)*(height//cn)
        if cur > boxes[i]:
            cur = boxes[i]
        ans += cur - before*8
        before = cur
print(ans)