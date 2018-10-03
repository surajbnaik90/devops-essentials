numbers = range(0,100)
my_range = numbers[0:50:5]
print(my_range == range(0,50,5))

#Print numbers in the reverse order
#Approach 1
testNumbers = range(0,10)
print("Print numbers using approach 1: ")
for i in testNumbers[::-2]:
    print(i)

#Approach 2
print("Print numbers using approach 2: ")
for i in range(9,0,-2):
    print(i)

print(range(0,10)[::-2] == range(9,0,-2))

#Back string example
backString = "...nohtyP gninraeL ma I"
print(backString[::-1])

