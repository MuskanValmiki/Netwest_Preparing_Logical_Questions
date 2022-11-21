# factorial
# def fact(a):
#     if a==0 or a==1:
#         return 1
#     else:
#         return a*fact(a-1)
# print(fact(5))

# fabonacci series
# def recur_fibo(n):
#    if n<=1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms=10
# if nterms<=0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))

# def fib(n):
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)
# for i in range(0,5):
#     print(fib(i))
    
# sum of numbers in an array
# def sumArray(array):
#     if len(array)==0:
#         return 0
#     else:
#         return array[0]+sumArray(array[1:len(array)])
# print(sumArray([1,2,3,4,5]))

# reverse a string
# def rev(s):
#     if len(s)==0:
#         return ""
#     else:
#         return s[len(s)-1]+rev(s[0:len(s)-1]) #s[-1]+rev(s[0:len(s)-1])
# print(rev("abcde"))

# power of number
# def pow(x,num):
#     if num==0:
#         return 1
#     else:
#         return x*pow(x,num-1)
# print(pow(2,5))

#print before my name all element
# def out( arr,i):
#     if arr[i] == "M":
#         return arr[i:]
#     else:
#         return out(arr, i-1)
# arr = ["P","J","R","K","S","M","G","L","N","C"]
# n = len(arr)
# print(out(arr,n-1))

# result=[]
# def find(arr,result):
#     if arr[0]=="G":
#         return ""
#     else:
#         result.append(arr[0])
#         return find(arr[1:],result)
# print(find(["P","J","R","K","S","M","G","L","N","C"],result))
# print(result)

# Bubble sort assending
# def BubbleSort(arr,n):
#     if n!=0:
#         for i in range(0,n-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#             else:
#                 BubbleSort(arr,n-1)
# arr=[15,78,3,6,8,35,98]
# n=7
# BubbleSort(arr,n)
# print(arr)

# Bubble sort desending
# arr=[1,18,14,13,3,5]
# n=6
# def bubble(arr,n):
#     for i in range(0,n-1):
#         if arr[i]<arr[i+1]:
#             arr[i],arr[i+1]=arr[i+1],arr[i]
#     if n>0:
#         bubble(arr,n-1)
# bubble(arr,n)
# print(arr)

#Continue Subarray
# def subArrays(arr,i,last):  
#     if last==len(arr):
#         return 0
#     elif i>last:
#         return subArrays(arr,0,last+1)
#     else:
#         print(arr[i:last+1])
#         return subArrays(arr,i+1,last)
# arr = [98, 25, 35,21,100]
# subArrays(arr, 0, 0)

# Selection Sort:-in selection sort we have to find min and then comepare in 
# right side then swap place of that element.
# arr=[5,2,4,1,3]
# result=[]
# def selectionSort(arr,result):
#     if len(arr)==0:
#         return ""
#     else:
#         j=arr.index(min(arr))
#         arr[0],arr[j]=arr[j],arr[0]
#         result.append(arr[0])
#         return selectionSort(arr[1:],result)
# selectionSort(arr,result)
# print(result)

# insertion sort:-in insertion sort we have to make key then compare all 
# the element of left side.key should be max if it is greater so we can 
# compare then swap in place or left.
# def insertion_sort(arr,Len):
#     if Len<=1:
#         return
#     insertion_sort(arr,Len-1)
#     end=arr[Len-1] 
#     i=Len-2
#     while(i>=0 and arr[i]>end):
#         arr[i+1]=arr[i]
#         i=i-1
#     arr[i+1]=end
#     return arr
# array=[9, 1, 7, 3, 5]
# print(insertion_sort(array, len(array)))

# convert into camel case
# string="over the lazy dog"
# new=''
# string_small=string.lower()
# string1=string_small.split()
# new=new+string1[0]
# for i in range(1,len(string1)):
#     a=string1[i].capitalize()
#     new=new+a
# print(new)




    


        