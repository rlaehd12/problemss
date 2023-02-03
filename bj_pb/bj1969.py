import sys
sys.stdin = open("input1969.txt")


genom_word_lst = 'ACGT'

n, length = map(int, input().split())
genom_lst = []
wordlst = ''
lst = [0] * length

for i in range(n):
    genom = input()
    genom_lst.append(genom)
#print(genom_lst)

for i in range(length):
    mystr = ''
    word4 = []
    for j in range(n):
        mystr += genom_lst[j][i]
    #print(mystr)
    # wordlst += (max(mystr, key=mystr.count))
    # lst[i] = max(mystr.count('T'), mystr.count('A'), mystr.count('G'), mystr.count('C'))
    for word in genom_word_lst:
        word4.append(mystr.count(word))
    
    lst[i] = max(word4)
    wordlst += genom_word_lst[word4.index(lst[i])]

    pass

print(wordlst)
print(n*length - sum(lst))