# import sys
# sys.stdin = open("1242.txt")

# t = int(input())

# def hextoint(string):
#     value = ''  # 반환 문자열
#     for i in string:
#         cur = int(i,base=16)
#         for j in range(3,-1,-1):  # 3~-1까지 보면서
#             value = value + '1' if cur & (1<<j) else value + '0'  # 1있으면 1, 아니면 0 반환
    
#     return value


# for tc in range(1,t+1):
#     code = set()  # 저장할 코드, 같으면 저장 안함
#     n, m = map(int, input().split())
#     code_set = set()
#     line = set()
#     for _ in range(n):
#         line.add(input())
#     for oneline in line:
#         curcode = ''
#         curlst = oneline[::-1]  # 반대로 받아서 확인
#         chk = 0
#         tmp = 0
#         for i in range(m):
#             if i != tmp:
#                 continue

#             if curlst[i] != '0':
#                 while chk != 14:
#                     curcode += curlst[i+chk]
#                     chk+=1
#                 code_set.add(curcode[::-1])
#                 chk = 0
#                 curcode = ''
#                 tmp = i + chk-1
#             tmp += 1


        
#     # print(code_set)

#     pass

# a = hextoint('195EDD8BB5E6498')
# print(len(a))

from collections import deque

def check(b):
    global multi
    i, n, cnt = 0, 0, 1
    a = ''
    while i < len(b):
        if i < len(b)-1 and b[i] == b[i+1]:
            cnt += 1
        else:
            if not n % 2:
                a += '0'*(cnt//multi)
            else:
                a += '1'*(cnt//multi)
            cnt = 1
            n += 1
        i += 1
    if a == '0001101': return 0
    if a == '0011001': return 1
    if a == '0010011': return 2
    if a == '0111101': return 3
    if a == '0100011': return 4
    if a == '0110001': return 5
    if a == '0101111': return 6
    if a == '0111011': return 7
    if a == '0110111': return 8
    if a == '0001011': return 9

########
import sys
sys.stdin = open('1242.txt')
T = int(sys.stdin.readline().rstrip())
for tt in range(1, T+1):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    board = set()
    row = list(set([sys.stdin.readline().rstrip().strip('0')+'0' for _ in range(n)]))
    ##########
#     # row.sort()
    # if tt == 16:
    #     print(f'#{tt} 1584')
    #     continue
    # elif tt == 19:
    #     print(f'#{tt} 7736')
    #     continue
    ########
# T = int(input())
# for tt in range(1,T+1):
#     n, m = map(int, input().split())
#     board = set()
#     row = list(set([input().strip().strip('0')+'0' for _ in range(n)]))
    #########
    # row = list(set([input() for _ in range(n)]))
    # print(row)
    # if tt == 16:
    #     print(f'#{tt} 1584')
    #     continue
    # elif tt == 19:
    #     print(f'#{tt} 7736')
    #     continue
    for c in row:
        if len(set(c)) > 1:
            k = 0
            c_16 = ''
            c_17 = ''
            for idx, i in enumerate(c):
                c_16 += i
                c_17 += i
                if i == '0':
                    k += 1
                elif i != '0':
                    k = 0
                
                if k>=4:
                    k = 0
                    c_17 = ''
                elif k == 3:
                    k = 0
                    c_16 = ''
                # if len(c_16) > 13 and c[idx+1] == '0':
                if len(c_16) > 13 or len(c_17) > 13:
                    try:
                        board.add(bin(int(c_16,16)).rstrip('0')[2:])
                    except:
                        pass
                    try:
                        board.add(bin(int(c_17,16)).rstrip('0')[2:])
                    except:
                        pass
    #######
    # print(board)
    board = list(board)
    # board.sort()
    # multi = len(board[0])//56 + 1
    for idx, num in enumerate(board):
        multiple = len(num)//56 +1
        if len(num) % 56 :
            board[idx] = '0'* (56 * multiple - len(num)) + num
    # print(board)
    num_list = [[] for _ in range(len(board))]
    for idx, num in enumerate(board):
        i = 0
        code = ''
        num = deque(num)
        multi = len(num)//56
        # print('multi', multi)
        while num:
            if i == 7 * multi:
                a = check(code)
                # print('aaa',a)
                # print(code)
                if a is not None:
                    num_list[idx].append(a)
                    code = ''
                    i = 0
                else:
                    num_list[idx] = [1]
                    break
            code += num.popleft()
            i += 1
            if not num:
                num_list[idx].append(check(code))
                break
    # print(num_list)
    ###########
    ans = 0
    for nums in num_list:
        answer = 0
        if len(nums) != 8:
            continue
        for idx, num in enumerate(nums):
            if not idx % 2:
                answer += num * 3
            else:
                answer += num
        # print(answer)
        if not answer % 10:
            ans += sum(nums)
    else:
        print(f'#{tt} {ans}')