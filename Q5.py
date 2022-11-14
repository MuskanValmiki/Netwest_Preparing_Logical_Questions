# Average Number

T = int(input())
for i in range(T):
    n,k,v = map(int,input().split())
    arr= list(map(int,input().split()))
    t = n + k 
    avg = t * v 
    s = sum(arr)
    s1 = avg - s
    if (s1>0) and s1%k==0:
        print(s1//k)
    else:
        print(-1)