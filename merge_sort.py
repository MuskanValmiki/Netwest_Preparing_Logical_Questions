# In merge sort we have to divide array in equal
# part till it did not became one element .
# then we compare and at last when all are 
# sorting so we have to again make one array and print.
# if our length will be odd so we divide even 
# number left and odd number right then same.

arr=[31,2,3,55,1,66,99,100,3,12]
def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergeSort(left)
        mergeSort(right)
        left_index=0
        right_index=0
        position=0
        while left_index<len(left) and right_index<len(right):
            if left[left_index]<right[right_index]:
                arr[position]=left[left_index]
                left_index+=1
            else:
                arr[position]=right[right_index]
                right_index+=1
            position+=1
        while left_index<len(left):
            arr[position]=left[left_index]
            position+=1
            left_index+=1
        while right_index<len(right):
            arr[position]=right[right_index]
            position+=1
            right_index+=1
    return arr
print(mergeSort(arr))