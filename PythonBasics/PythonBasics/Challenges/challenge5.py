#Create a program that takes some text and returns a list of all the characters 
# in the text that are not vowels, sorted in alphabetical order.

text = str(input("Please enter some text: "))

vowels = {'a', 'e', 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
consonants_list = set()

for char in text:
    if char not in vowels:
        consonants_list.add(char)

sortedlist = sorted(consonants_list)
print(sortedlist)

#Other way if doing the same thing
print("-" * 100)
sometext = "Hey I am learning Python"
print(sometext)

vowels = frozenset("aeiou")
newSet = set(sometext).difference(vowels)

print("New set is {}".format(sorted(newSet)))
