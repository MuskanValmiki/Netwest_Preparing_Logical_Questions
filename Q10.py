# odd repeat

T=int(input())
for i in range(T):
    N,K,S=map(int,input().split())
    Temp=S-(N**2)
    print(Temp//(K-1))
    