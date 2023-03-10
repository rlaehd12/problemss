D,P,Q = map(int, input().split())
big = max(P, Q)
small = min(P,Q)
i = 0
j = D//big + 1
chai = big//small
cur = (big*j) - D
ans = big*j
if D<=small:
    ans = small
elif D<= big:
    if D%small==0:
        ans = D
    elif big-D < (D//small+1)*small-D:
        ans = big
    else:
        ans = (D//small+1)*small
else:
    while j>0:
        if cur == 0:
            break
        j-=1
        i+=chai
        s = (small*i + big*j)

        if s - D>=0:
            while s-D>=0:
                i-=1
                s = (small*i + big*j)
            i+=1
            s = (small*i + big*j)
            if cur>s-D:
                cur = s-D
                ans = s
        else:
            i+=1
            s = (small*i + big*j)
            if cur>s-D:
                cur = s-D
                ans = s
        print(i,j,s)
print(ans)