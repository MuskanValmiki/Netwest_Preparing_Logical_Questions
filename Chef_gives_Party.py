T=int(input())
for i in range(T):
    N,X,K=map(int,input().split())
    if X*N<=K:
        print("YES")
    else:
        print("NO")