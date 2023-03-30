def merge(left, right):
    # 병합 알고리즘 적용
    tmp = []
    l = 0
    r = 0
    flag = 0
    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right):
            if left[l] <= right[r]:
                tmp.append(left[l])
                l += 1
            else:
                tmp.append(right[r])
                r += 1
        elif l < len(left):
            if flag == 0:
                ans[0] +=1
                flag = 1
            tmp.append(left[l])
            l += 1
        elif r < len(right):
            tmp.append(right[r])
            r += 1
    # print(tmp)
    return tmp

# 분할과정(수정 전)
## 배열 m을 통째로 받아서 분할
def msort(m):
    if len(m) == 1:
        return m
    mid = len(m)//2
    # 원본과 같은 크기의 배열이 또 만들어짐
    # 메모리 너무 많이 먹음
    left = m[0:mid]
    right = m[mid:]
    
    left = msort(left)
    right = msort(right)

    return merge(left, right)

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0]
    a = msort(arr)
    print(a)
    print(f'#{tc} {a[n//2]} {ans[0]}')