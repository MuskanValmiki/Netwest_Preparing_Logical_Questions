T=int(input())
for i in range(T):
    N= map(int,input().split())
    arr=list(map(int,input().split()))
    # if (int(N)/int(arr))%2 == 0:
    l=len(arr)
    if N/l%2==0:
        print("Yes")
    else:
        print("No")