def search(arr,x):
    left = 0
    right = len(arr)-1
    mid = int((left+right)/2)
    bool = False
    while left <= right:
        if x == arr[mid]:
            bool = True
            break
        elif x < arr[mid]:
            right = mid - 1
            mid = int((left+right)/2)
        elif x > arr[mid]:
         left = mid + 1
        mid = int((left + right)/2)
    if bool == True:
        return mid
    else:
        return -1

arr=[1,2,3,4,5,6,7,8,9]
x = 2354
print(search(arr,x))
