even = [2,4,6,8,10]
odd = [1,3,5,7,9]

#List concatenation and sorting
numbers = even + odd
print("Concatenated numbers are: {}".format(numbers))

numbers.sort()
print("Sorted numbers using .sort() are : {} ".format(numbers))

sorted_numbers = sorted(even+odd)
print("Sorted numbers using 'sorted' function are : {} ".format(numbers))
print("")

#Lists Comparision
print("Comparing list {} with {}".format(even+odd, sorted_numbers))
if (even+odd) == sorted_numbers:
    print("Lists are equal")
else:
    print("Lists are not equal")

#Lists Comparision
print("")
print("Comparing list {} with {}".format(sorted_numbers, sorted(numbers)))
if sorted_numbers == sorted(numbers):
    print("Lists are equal")
else:
    print("Lists are not equal")

