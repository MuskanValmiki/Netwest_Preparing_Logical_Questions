# Daily Train

from math import factorial
X,N=map(int,input().split())
ans=0
for i in range(N):
    String=input()
    car_places=54
    for j in range(9):
        value=str(String[j*4:j*4+4]+String[car_places-2:car_places])
        car_places-=2 
        comb=value.count("0")
        if(comb>X):
            ans+=factorial(comb)/(factorial(comb-X)*factorial(X))
        elif(X==comb):
            ans+=1 
print(int(ans))

