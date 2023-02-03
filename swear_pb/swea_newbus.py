

def what_bus(bus):
    my_bus = []
    if bus[0] == 1:  # 일반
        for i in range(bus[1],bus[2] + 1):
            my_bus.append(i)
        return my_bus
    elif bus[0] == 2:  # 급행
        for i in range(bus[1], bus[2] + 1, 2):
            my_bus.append(i)
        return my_bus

    else:  # 광역 급행
        if (bus[1] % 2) == 0:  # 짝수면
            for i in range(bus[1], bus[2] + 1):
                if i % 4 == 0:
                    my_bus.append(i)
            return my_bus

        else:  # 홀수면
            for i in range(bus[1], bus[2] + 1):
                if i % 3 == 0:
                    my_bus.append(i)
            my_bus = [item for item in my_bus if (item % 10) != 0]

            return my_bus
        pass

T = int(input())

for test_case in range(1, T + 1):
    bus_lst = []
    ans_lst = [0] * 1001

    n = int(input())  # 노선 개수
    for i in range(n):
        bus = list(map(int, input().split()))
        bus_lst.append(what_bus(bus))
    
    # for i in bus_lst[0]:
    #     count = 0
    #     pass
    #     for j in range(len(bus_lst)):
    #         if i in bus_lst[j]:
    #             count += 1
    #     if ans < count:
    #         ans = count
    #     pass

    for i in range(n):
        for j in bus_lst[i]:
            ans_lst[j] += 1
        pass

    # print(ans_lst)
    print(len(bus_lst))
    print(f'#{test_case} {max(ans_lst)}')
    pass