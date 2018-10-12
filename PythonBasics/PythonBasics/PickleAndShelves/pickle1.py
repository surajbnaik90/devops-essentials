#Using 'Pickle' to write binary files
#Imp Note : Pickle make use of protocols while dumping and reading data.

import pickle

tupleObject = ('Microsoft', 'Azure', 'Satya Nadella')

with open("testfile.pickle","wb") as pickle_file:
    pickle.dump(tupleObject, pickle_file)


#Read the binary file
with open("testfile.pickle", "rb") as pickle_file:
    obj = pickle.load(pickle_file)
print(obj)

#Dump tuple and some integer values to the binary file
print("-" * 60)
print("Dump tuple and some integer values to the binary file...")
even_numbers = list(range(0,10,2))
odd_numbers = list(range(1,10,2))

with open("testfile.pickle","wb") as pickle_file:
    pickle.dump(tupleObject, pickle_file)
    # or pickle.dump(tupleObject, pickle_file, protocol=pickle.DEFAULT_PROTOCOL
    # or pickle.dump(tupleObject, pickle_file, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even_numbers, pickle_file)
    pickle.dump(odd_numbers,pickle_file)
    pickle.dump("Some text", pickle_file)

print("Done")
print("Now read from the file created...")
#No read the entire binary file
with open("testfile.pickle", "rb") as pickle_file:
    obj = pickle.load(pickle_file)
    even_list = pickle.load(pickle_file)
    odd_list = pickle.load(pickle_file)
    sometext = pickle.load(pickle_file)

print(obj)
print(even_list)
print(odd_list)
print(sometext)
print("-" * 60)