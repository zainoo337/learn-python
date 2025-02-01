list =[-1] * 1000
list[0]=1
list[1]=1
def factorial(n):
    if list[n]!=-1:
        return list[n]
    
    
    list[n]=(n)*factorial(n-1)
    return list[n]
print(factorial(5))



# n = 7
# 6
# factorial(2)  -> 2
# factorial(1) -> 1