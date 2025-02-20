array=[78,45,23,89,34,47]
n=len(array)
for i in range(0,n):
    for j in range(0,n-1):
        if array[j] > array[j+1]: 
            temp=array[j+1]
            array[j+1]=array[j]
            array[j]=temp
print(array)