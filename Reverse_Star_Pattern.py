N=int(input())
for i in range (N):   
    for j in range(i,N):
        print(" ",end=" ")
    for j in range (i+1):
        print("*",end="")
    print( )



N=map(int,input().split())
i=0
while i<N:
    j=i
    while j<N:
        print(" ",end="")
        j+=1
    j=0
    while j<i+1:
        print("*",end="")
        j+=1
    print()
    i+=1
    
        