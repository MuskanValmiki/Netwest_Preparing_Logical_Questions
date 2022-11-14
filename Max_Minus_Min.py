T=int(input())
for i in range(T):
    A,B,C=map(int,input().split())
    maximum=max(A,B,C)
    minimum=min(A,B,C)
    print(maximum,minimum)
    