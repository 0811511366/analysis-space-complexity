def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        if target<arr[mid]:
            return mid-1
        else:
            left=mid+1
    return -1

array= [1, 3, 5, 7, 9, 11]
target=7
result=binary_search(array,target)
if result !=-1:
    print("element found at index: ",result)
else:
    print("element not found")