import sys
sys.stdin = open("16440.txt")

n = int(input())
lst = input()

print(lst)

# 절반만큼 이동하면서 가장 엔트로피 낮은 집합 찾기
## 찾았으면 남은 엔트로피 크기만큼 이동하며 찾기
### 엔트로피 0일때까지 위 반복