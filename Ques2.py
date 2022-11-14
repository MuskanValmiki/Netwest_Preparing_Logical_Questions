# in dictionary we can store our data by using key and value pair .
# it did not allow duplicate.
# in dictinary we can separeate our key and value by using :
# dictinary difine with {}.
# it is order meand line by line it goes.
# it is mutable means we can add and remove also.
# in dictinary key should be in string only.
dic={"1":"one","2":"two","3":"three","4":"four"}

# in dictinary we can add key and value 
dic["coll"]="98"
print(dic)

# here we are printing specific value of dictionary  by using key
print(dic["2"])

# here we remove the value from dictionary by using key 
dic.pop("3")
print(dic,"new")

# if we use popitem so it remove last value of dictionary
dic.popitem()
print(dic,'###################')

# order means it run one by or check one by one by using key 
dic={"1":"one","2":"two","3":"three","4":"four"}
for key in dic:
    print(key,"here we print key") 
    print(dic[key],"here we want value so we use dic and key")
    
# if we want to find length of dictionary so we use len function
dic={"1":"one","2":"two","3":"three","4":"four"}
print(len(dic),"length")

# here if we gave duplicate key in case so it gave us updated value
dic={"1":"one","2":"two","3":"three","4":"four","1":"musssu"}
print(dic,'updating ')

# if we want to get key and value without using loop so we can use items() function
dic={"1":"one","2":"two","3":"three","4":"four"}
print(dic.items(),"here we get value of dictionary")
    
# 
# in dictionary we can store our data by using key and value pair .
# it did not allow duplicate.
# in dictinary we can separeate our key and value by using :
# dictinary difine with {}.
# it is order meand line by line it goes.
# it is mutable means we can add and remove also.
dic={"1":"one","2":"two","3":"three","4":"four"}

# in dictinary we can add key and value 
dic["coll"]="98"
print(dic)

# here we are printing specific value of dictionary  by using key
print(dic["2"])

# here we remove the value from dictionary by using key 
dic.pop("3")
print(dic,"new")

# if we use popitem so it remove last value of dictionary
dic.popitem()
print(dic,'###################')

# order means it run one by or check one by one by using key 
dic={"1":"one","2":"two","3":"three","4":"four"}
for key in dic:
    print(key,"here we print key") 
    print(dic[key],"here we want value so we use dic and key")
    
# if we want to find length of dictionary so we use len function
dic={"1":"one","2":"two","3":"three","4":"four"}
print(len(dic),"length")

# here if we gave duplicate key in case so it gave us updated value
dic={"1":"one","2":"two","3":"three","4":"four","1":"musssu"}
print(dic,'updating ')

# if we want to get key and value without using loop so we can use items() function
dic={"1":"one","2":"two","3":"three","4":"four"}
print(dic.items(),"here we get value of dictionary")
    
# syntex of loop 
# for loop is finite loop
# while loop is infinite loop
for i in range(1,10):
    pass

i=0
while i<=10:
    pass

