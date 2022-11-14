for i in range(int(input())):
    n,x,y=map(int,input().split())
    z=x+y*2
    if n>=z:
        print('YES')
    else:
        print("NO")