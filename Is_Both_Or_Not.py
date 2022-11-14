# N=int(input())
N=map(int(input().split()))
if N%5==0 and N%11==0:
    print("BOTH")
elif N%5==0 or N%11==0:
    print("ONE")
else:
    print("NONE")
    
    
    
    
    
