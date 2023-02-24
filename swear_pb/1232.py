import sys
sys.stdin = open("1232.txt")


def evaluate_postfix(expression):  #gpt가 만들어줌
    stack = []
    operators = set(['+', '-', '*', '/', '^'])
    for char in expression:
        if char not in operators:
            stack.append(int(char))
        else:
            num2 = stack.pop()
            num1 = stack.pop()
            if char == '+':
                result = num1 + num2
            elif char == '-':
                result = num1 - num2
            elif char == '*':
                result = num1 * num2
            elif char == '/':
                result = num1 / num2
            elif char == '^':
                result = num1 ** num2
            stack.append(result)
    return int(stack.pop())

def postorder(t):
    if t != 0:  # 범위 안이면
        postorder(c1[t])
        postorder(c2[t])
        st.append(item[t])


for tc in range(1,11):

    n = int(input())
    item = [0] * (n+1)
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)
    st = []
    ans = 0


    for i in range(n):
        lst = input().split()
        idx = int(lst[0])
        item[idx] = lst[1]

        try: c1[idx] = int(lst[2])
        except: pass

        try: c2[idx] = int(lst[3])
        except: pass

    postorder(1)
    
    ans = evaluate_postfix(st)

    print(f'#{tc} {ans}')

# def cal(n,tree):
#     n = int(n)
#     if tree[n][0] == '+':
#         return cal(tree[n][1],tree) + cal(tree[n][2],tree)
#     elif tree[n][0] == '-':
#         return cal(tree[n][1],tree) - cal(tree[n][2],tree)
#     elif tree[n][0] == '*':
#         return cal(tree[n][1],tree) * cal(tree[n][2],tree)
#     elif tree[n][0] == '/':
#         return cal(tree[n][1],tree) // cal(tree[n][2],tree)
#     else:
#         return int(tree[n][0])
          
 
 
# T = 10
# for test_case in range(1,T+1):
#     N = int(input())
#     lst = [0] *  (N + 1)
#     for _ in range(N):
#        n, *m =  input().split()
#        print(m, end=' ')
#        lst[int(n)] = m
#     print(f'#{test_case} {cal(1,lst)}')
