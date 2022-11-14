# cook your dish here
n=int(input())
points = list(map(int, input().split()))
n-=1 
while(n>=0):
    print(points[n],end=" ")
    n=n-1
