# cook your dish here
N=int(input())

for i in range (N):
    
    for j in range(i,N):
        print(" ",end=" ")
    for j in range (i+1):
        print("*",end="")
    print( )