length, width, height = map(int, input().split())
N = int(input())
boxes = [0] * 21  # 내가 가진 박스
for _ in range(N):
    a, b = map(int, input().split())
    boxes[a] = b
# print(boxes)
# 부피 확인
V = length*width*height
ans = 0  # 채워 넣은 박스개수
total = 0  # 채워 넣은 부피
# 가장 큰 박스부터 넣으면서 확인
for i in range(20,-1,-1):
    cur_box = 2**i

    total *= 8
    cur = (length//cur_box)*(width//cur_box)*(height//cur_box) - total
    cur = boxes[i] if boxes[i] <= cur else cur

    total += cur
    ans += cur

if total < V:  # 전체 부피보다 작으면 못채운거임
    print(-1)
else:
    print(ans)
