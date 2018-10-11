#Read & write file
file = open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\sample.txt",'r')
for line in file:
    print(line, end='')
file.close()
print("\n")
print("*" * 100)

#Read & write using 'with': No need to close the file
with open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\sample.txt",'r') as file:
    for line in file:
        print(line, end='')

print("\n")
print("*" * 100)

#Read & write using 'while': No need to close the file
with open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\sample.txt",'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()
print("\n")
print("*" * 100)

#Read & write using 'readlines': No need to close the file
with open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\sample.txt",'r') as file:
    lines = file.readlines()
    
for line in lines:
    print(line, end='')
print("\n")
print("*" * 100)