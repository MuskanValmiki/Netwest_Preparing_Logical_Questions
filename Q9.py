# Coronavirus Spread

T=int(input())
for i in range(T):
    N=int(input())
    L=list(map(int,input().split()))
    C=1
    M=[]
    for i in range(N-1):
        if L[i+1]-L[i]<=2:
            C+=1
        else:
            M.append(C)
            C=1
    M.append(C)
    print(min(M),max(M))