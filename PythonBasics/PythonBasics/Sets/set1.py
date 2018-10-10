#Creating sets
companies = {"Microsoft", "Amazon", "Google"}
print(companies)

for company in companies:
    print(company)

print("-" * 100)

companies_set = set(["Microsoft", "Amazon", "Google"])
print(companies_set)

for company in companies_set:
    print(company)

#Add item to a set
companies.add("VMWare")
companies_set.add("VMWare")
print(companies)
print(companies_set)

#Create an empty set
emptyset = set()
emptyset2 = {}

emptyset.add("test")
#emptyset2.add("test") - throws an error

#Creating set from other objects
even = set(range(0,10,2))
print(even)

odd_tuple = (1,3,5,7,9)
odd = set(odd_tuple)
print(odd)

print("-" * 100)

#Union of sets
setA = {4, 12, 36, 8, 20}
setB = {2, 4, 6 , 8, 10}
print("Set A : {}".format(setA))
print("Set B : {}".format(setB))

print("Union of sets...")
print(setA.union(setB))
print("Length of the union of sets : {}".format(len(setA.union(setB))))

#Intersection of sets
print("Intersection of sets...")
setA.intersection(setB)
print(setA & setB)

#Subtraction of sets
print("Subtraction of sets...")
print("A - B = {}".format(sorted(setA.difference(setB))))
print("B - A = {}".format(sorted(setB-setA)))
