n = int(input())
c = 0
for i in range(1, n + 1):
    if(i % 2 != 0):
        print(c+1, c+2, c+3, c+4, c+5)
    else:
        print(c+5, c+4, c+3, c+2, c+1)
    c+=5



N=map(int,input().split())
c=0
i=1
while i<=N:
    if i%2!=0:
        print(c+1,c+2,c+3,c+4,c+5)
    else:
        print(c+5,c+4,c+3,c+2,c+1)
    c+=5
    i+=1