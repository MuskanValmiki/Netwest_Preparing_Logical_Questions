T=int(input())
for i in range(T):
    n,b=map(int,input().split())
    list=list(map(int,input().split()))
    ans=0
    for j in range(0,n):
        ans+=list[j]
    if ans>b:
        print("YES")
    else:
        print("NO")
        