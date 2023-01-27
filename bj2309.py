import sys
sys.stdin = open('input2309.txt')

dwarf = []

for i in range(9):
    dwarf.append(int(input()))

#print(dwarf)
sum_of = sum(dwarf)

for i in range(9):
    for one in dwarf[i+1:]:
        #print(one, end= ' ')
        if (dwarf[i] + one) == (sum_of - 100):
            #print(dwarf[i], one)
            a = dwarf[i]
            b = one

dwarf.remove(a)
dwarf.remove(b)

for i in sorted(dwarf):
    print(i)