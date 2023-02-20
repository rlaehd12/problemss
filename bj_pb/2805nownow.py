import sys
sys.stdin = open("2805.txt")


def binary(low, high, target):
    ans = 0
    mid = (low + high) // 2
    for tree in lst:
        ans = ans + (tree - mid) if tree - mid > 0 else ans

    if low < high:
        if ans > target:
            low = mid + 1
            binary(low, high, target)
        elif ans < target:
            high = mid - 1
            binary(low, high, target)
        else:
            print(mid)
            return
    else:
        print(mid+1)


n, m = map(int, input().split())
lst = list(map(int, input().split()))

low = max(lst) - m
high = max(lst)

# print(lst, low, high)
binary(low, high, m)