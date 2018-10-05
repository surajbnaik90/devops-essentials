#Note: Tuple object doesn't support item assignment.

record1 = "Microsoft", "Azure", "Satya Nadella"
record2 = "Amazon", "AWS", "Jeff Bezos"
record3 = "Google", "GCP", "Sundar Pichai"

print(record2)
print(record1[1])

#record1[2] = "Scott Guthrie" - Will throw an error.
# Tuple objects are immutable and are intended to hold heterogeneous items.
print(record1)

#But you can do this with Tuples - An important concept.
record1 = record1[0], record1[1], "Scott Guthrie"
print(record1)

data1 = ["Microsoft", "Azure", "Satya Nadella"]
data1[2] = "Scott Guthrie"   #Correct usage. Lists are mutable.
#and are intended to hold homogeneous items.
print(data1)

#Unpacking Tuples
print("Unpacking tuple {}".format(record2))

company, cloud, ceo = record2

print("Company : {} ".format(company))
print("Cloud : {} ".format(cloud))
print("CEO : {} ".format(ceo))