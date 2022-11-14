T=int(input())
for i in range(1,T+1):
    X,Y,Z=map(int,input().split())
    if Y%Z==0:
        print(X*(Y//Z))
    else:
        print(X*(Y//Z+1))