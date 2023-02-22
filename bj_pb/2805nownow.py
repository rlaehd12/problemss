import sys
sys.stdin = open("2805.txt")


def binary(low, high, target):
    result = 0
    while low <= high:
        ans = 0
        mid = (low + high) // 2
        for tree in lst:
            ans = ans + (tree - mid) if tree - mid > 0 else ans

        if ans >= target:
            low = mid + 1
            result = mid
        else:
            high = mid - 1
    return result


n, m = map(int, input().split())
lst = list(map(int, input().split()))

low = max(lst) - m
high = max(lst)

# print(lst, low, high)
print(binary(low, high, m))