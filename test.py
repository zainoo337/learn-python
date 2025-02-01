list= [-1] * 10000
list[0]= 0
list[1]= 1



def function(n):
    if list[n]!= -1:
        return list[n]
    
    
    
    list[n]=function(n-1)+function(n-2)
    return list[n]
print(function(100))
for i in range(0,9):
    print(list[i])




# function(5) -> 5
# function(4) -> 3
# function(3) -> 2
# function(2) -> 1
# 1+0