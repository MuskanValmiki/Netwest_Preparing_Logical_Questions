T=int(input())
for i in range(T):
    A,B=map(int,input().split())
    Total=A+B 
    c=0
    for j in range(1,Total):
        if Total%j==0:
            c+=1 
    if c==1:
        print("Alice")
    else:
        print("Bob")
        