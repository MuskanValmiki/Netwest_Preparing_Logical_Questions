T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    if B%A==0:
        print("YES")
    else:
        print("NO")