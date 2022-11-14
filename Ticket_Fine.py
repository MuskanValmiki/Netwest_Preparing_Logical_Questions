for i in range(int(input())):
    s=input()
    x=len(set(s))
    if(x==2):
        for j in range(len(s)-1):
            if(s[j]==s[j+1]):
                print("N0")
                break 
        else:
            print("YES")
    else:
        print("NO")
