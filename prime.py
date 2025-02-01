
while True:
    x = int(input("enter a number"))
    y = 1
    count = 0
    while y <= x:
        if x % y == 0:
            count += 1
        y +=1
    if count == 2:
        print(f"{x} is a prime number")
    else:
        print(f"{x} is not a prime number")


    
# x=4
# y=1,2,3,4
# count =1,2,3