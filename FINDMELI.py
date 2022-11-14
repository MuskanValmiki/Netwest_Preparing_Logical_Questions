# cook your dish here
N, K = map(int,input().split())
lis=map(int, input().split())
A=list(lis)
if  K in A:
    print(1)
else:
    print(-1)


