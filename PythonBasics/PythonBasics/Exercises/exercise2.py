#Write a program to print all the numbers from 0 to 100 that are divisible by 6

for i in range(0,100):
    if i%6 == 0 :
        print(i)

#Or
# This solution uses a slice
#for i in range(100)[::6]:
#   print(i)