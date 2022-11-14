# factor in recusrion
def recursion(a):
    if a==1:
        return 1
    else:
        return a*recursion(a-1)
print(recursion(5))

# const recursion=(a)=>{
#     if(a==1){
#         return 1
#     }
#     else{
#         return a*recursion(a-1)
#     }
# }
# console.log(recursion(5))


