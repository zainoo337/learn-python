arr=[1,2,3,4,5,6,7,8,9]
x = 1
left = 0
right = len(arr)-1
mid = int((left+right)/2)
bool = False 
while left <= right:
    if arr[mid] == x :
        bool = True
        break
    elif x < arr[mid]:
        right = mid -1 
        mid = int((left+right)/2)
    elif x > arr[mid]:
        left = mid + 1
        mid = int((left + right)/2)
if bool == True:
    print(f"{x} is found at {mid}")
else:
    print(f"{x} is not found")
        
    
        
    # x = 0
    # left = 0,5,7,8
    # right =8,
    # mid = 4,6,7,8
    
    
    