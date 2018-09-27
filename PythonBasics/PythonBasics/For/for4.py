#Write a program to print out all the numbers from 0 to 20 that aren't divisible by 3 or 5.

for i in range(0, 20):
    if i%3==0 or i%5==0:
        continue
    print(i)