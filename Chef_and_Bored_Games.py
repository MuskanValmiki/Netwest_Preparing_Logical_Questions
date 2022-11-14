
T=int(input())
for i in range(T):
    N=int(input())
    c=0
    for i in range(1, N+1,2):
        k=N-i+1
        c+=(k*k)
    print(c)