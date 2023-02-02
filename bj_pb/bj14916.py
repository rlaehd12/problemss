cost = int(input())

rest5 = cost//5
rest2 = 0
while rest5 >= 0:
    if (cost - (rest5 * 5)) % 2 == 0:
        rest2 = (cost - (rest5 * 5)) // 2
        break
    else:
        rest5 -= 1

print(rest5 + rest2)