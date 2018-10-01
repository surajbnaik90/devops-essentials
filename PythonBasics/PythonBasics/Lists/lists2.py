#Creating a new list

evenlist = []  #or evenlist = list() <=> creating an empty list

evenlist = [4,8,2,6,12,10]
print("Even List : {}".format(evenlist))

print("Assigning Even List to another even list")
anotherEvenList = evenlist #They now point to the same memory location. 

print("Another even list: {} ".format(anotherEvenList))
anotherEvenList.sort();
print("After sorting another even list: {} ".format(anotherEvenList))

print("Now the even list is : {} ".format(evenlist))
print("Conclusion is when we assign list to another list, they both point to the same memory location")

print("Printing even list in the reverse order: {}".format(sorted(evenlist,reverse=True)))
