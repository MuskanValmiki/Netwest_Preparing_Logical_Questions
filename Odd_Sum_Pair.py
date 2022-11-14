T=int(input())
for i in range(T):
    a,b,c=map(int,input().split())
    if(a+b)%2!=0 and (b+a)%2!=0:
        print("YES")
    elif(a+c)%2!=0 and (c+a)%2!=0:
        print("YES")
    elif(b+c)%2!=0:
        print("YES")
    else:
        print("NO")
        