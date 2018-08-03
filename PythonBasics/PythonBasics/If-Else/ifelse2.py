#Simple program to ask for a name and age.
#When both values have been entered, check if the person 
#is the right age to join senior citizens club (they must be over 60 and under 140 :D )
#If they are then welcome to the club, otherwise print a message refusing the entry.

name = input("Enter your name ")
age = int(input("Your age {0} ".format(name)))


if 60< age <140 :
    print("Welcome to the senior citizen club {0}".format(name))
else:
    print("Sorry, only people above 60 and under 140 are allowed")
