bool = False
list=[12,445,66,345,876,786]
x = 345
for i in range(0,len(list)):
    if list[i] == x:
        bool = True
        print(f"{x} is found")
        print(f"{i} is the index") 
if bool == False:
    print("number have not found")

     

