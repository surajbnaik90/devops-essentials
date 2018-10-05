#Tuple within tuple

record1 = "Microsoft", "Software Products", (
    "Visual Studio", ".NET Frameworks", "Visual Studio Code")

print(record1)

company, manufacture, products = record1
print(company)
print(manufacture)
print(products)
print(products[1])

for product in products:
    print(product)

#List in tuple
record2 = "Microsoft", "Software Products", (["Visual Studio", ".NET Frameworks", "Visual Studio Code"])
record2[2].append("Test")

print(record2[2])
