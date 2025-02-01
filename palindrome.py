word ="level"
i = 0
j = len(word) - 1
Palindrome = True
while i < j:
    if word[i] == word[j]:
        i += 1
        j -= 1
    else:
         Palindrome = False
         break
       

if Palindrome:
    print("Its a palindrome")
else:
    print("it is not a palindrome")
    
    

    
    
    
# i=0,1,2
# j=4,3,2 