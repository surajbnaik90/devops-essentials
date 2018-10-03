#Understanding ranges
numberlist = list(range(10))
print(numberlist)

even = list(range(0,10,2)) #Note how range is used inside the list(). 
odd = list(range(1,10,2))  # Just range() won't return list of numbers.

print(even)
print(odd)

#Please note this:
testnumbers = range(0,1000,3)
print(testnumbers[90])

#Check whether a given input is in the set
set = range(4, 1000,4)
userInput = int(input("Please enter a positive integer less than 1000: "))
if userInput in set:
    print("Input is in the set")