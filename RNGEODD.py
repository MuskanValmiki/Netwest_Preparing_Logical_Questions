# cook your dish here
L,R=map(int,input().split())
while L<=R:
    if L%2!=0:
        print(L,end=" ")
    L+=1
