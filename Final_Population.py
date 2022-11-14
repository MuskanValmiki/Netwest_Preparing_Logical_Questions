T=int(input())
for i in range(T):
    x,y,z=map(int,input().split())
    if y<=x:
        print(x-y+z)