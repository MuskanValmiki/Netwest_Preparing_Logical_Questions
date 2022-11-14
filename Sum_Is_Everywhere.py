N=int(input())
even_number=0
odd_number=0
for i in range (1,N*2+1):
    if i%2!=0:
        odd_number+=i
    else:
        even_number+=i
print(odd_number,even_number)



N=map(int,input().split())
even_sum=0
odd_sum=0
i=1
while i<N*2+1:
    if i%2!=0:
        odd_sum+=i
    else:
        even_sum+=i
    i+=1
print(odd_sum,even_sum)