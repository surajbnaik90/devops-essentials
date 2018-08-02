#Simple python if-else program asking the user to input a number
#and check whether or not the number is divisible by 3.

print("Please input a number between 1 and 20 ")
number = int(input())

if (number<1 or number>20):
	print("Please enter a number between 1 and 20")

number = int(input())
if number%3 == 0:
	print("Number is divisble by 3")
else:
	print("Number is not divisble by 3")