#Python program to make use of for loops and break statements.

for i in range(0, 100, 7):
    print(i)
    if i>0 and i%11==0:
        print("Breaking the loop as {0} is divisible by 11".format(i))
        break