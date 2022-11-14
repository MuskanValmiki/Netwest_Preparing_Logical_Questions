# cook your dish here
N=int(input())
count=0
num=" "
i=1
while i<=N:
    if N%i==0:
        count+=1
        num+=str(i)
        num+=" "
    i+=1
print(count)
print(num)

