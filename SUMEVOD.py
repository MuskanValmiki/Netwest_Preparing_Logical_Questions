# cook your dish here
N=int(input())
even_number=0
odd_number=0
for i in range (1,N*2+1):
    if i%2!=0:
        odd_number+=i
    else:
        even_number+=i
print(odd_number,even_number)