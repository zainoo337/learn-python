arr=[34,45,49,56,78,90]
x=94
left=0
right=len(arr)-1
mid = int((left + right)/2)
bool = False
while left <= right:
    if arr[mid] == x:
        bool = True
        break
    elif x > arr[mid]:
        left = mid+1
        mid = int((left + right)/2)
    elif x < arr[mid]:
        right = mid-1
        mid = int((left + right)/2)
if bool:
    print("found")
else:
    print("not found")

    
    
    
    

    