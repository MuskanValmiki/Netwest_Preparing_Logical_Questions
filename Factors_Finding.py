# cook your dish here
N=int(input())
distinct=0
number =[]
for i in range(1, N+1):
    if N%i==0:
        number.append(i)
        distinct=distinct+1
print(distinct)
for j in number: 
    print(j, end=" ")
    
    

N=map(int,input().split())
fact=0
list=[]
i=1
while i<=N:
    if N%i==0:
        list.append(i)
        fact+=1
    i+=1
print(list)
for j in list:
    print(j,end=" ")



# cook your dish here

N=map(int,input().split())
fact=0
list=[]
for i in range(1,N+1):
    if N%i==0:
        list.append(i)
        fact+=1
print(list)
