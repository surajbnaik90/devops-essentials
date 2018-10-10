#Modify the set after subtraction
setA = {4, 12, 36, 8, 20}
setB = {2, 4, 6 , 8, 10}
print("Set A : {}".format(setA))
print("Set B : {}".format(setB))

print("Modify the actual set after subtraction of sets...")
setA.difference_update(setB)
print("A - B = {}".format(sorted(setA)))
print("Set A : {}".format(sorted(setA)))

print("-" * 100)
setA = {4, 12, 36, 8, 20}
setB = {2, 4, 6 , 8, 10}
print("Symmetric difference of A & B is subtract (A-B) from sets A & B")
print("Hence, symmetric difference of A & B : {}".format(sorted(setA.symmetric_difference(setB))))

print("-" * 100)
print("Discard & Remove usage...")
setA.discard(12)
print("Discard 12 from set A : {}".format(setA))
setA.remove(36)
print("Remove 36 from set A : {}".format(setA))

#setA.remove(10) - throws an error
#Alternative is to check before remove
if 10 in setA:
    setA.remove(10)

setA.discard(10)
print("Discard 10 from set A : {} doesn't throw an error even though 10 doesn't exist.".format(setA))

#Subset and superset operations
print("-" * 100)
setA = {4, 6, 12, 36, 8, 20}
setB = {4, 6 , 8}
print("Set A : {}".format(setA))
print("Set B : {}".format(setB))

if setB.issubset(setA):
    print("Set B is a subset of set A")

if setA.issuperset(setB):
    print("Set A is a superset of set A")

#Frozen set - can't update the set
print("-" * 100)
setC = frozenset(range(0,10,2))
print("Frozen set C = {}".format(setC))
#setC.add(2) - will throw an error
