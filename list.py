numbers = [1,200,3,4,5,6]
maximum =numbers[0]
for elem in numbers:
    if elem <= maximum:
        maximum = elem
print(maximum)
