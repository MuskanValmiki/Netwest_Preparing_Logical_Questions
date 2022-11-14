# Vaccine Distribution

import math
T=int(input())
for i in range(T):
    N,D=map(int,input().split())
    l=list(map(int,input().split()))
    c1=0 
    c2=0 
    for j in range(len(l)):
        if l[j]>=80 or l[j]<=9:
            c1+=1
        else:
            c2+=1 
    print(math.ceil(c1/D)+math.ceil(c2/D))
