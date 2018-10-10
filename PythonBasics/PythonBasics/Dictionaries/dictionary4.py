#Get tuples from dictionary object.

products = {"Microsoft" : "Cloud computing platform - Azure ",
            "Amazon": "Amazon Web Services (AWS)",
            "Google": "Google Cloud Platform (GCP)"}

print(products.items())
print("-" * 60)

tuples = tuple(products.items())
print(tuples)

print("-" * 60)
print(dict(tuples))

#Add two dictionaries
print("-" * 60)
print("Add two dictionaries...")
products2 = {"VMWare" : "VMWare Cloud"}
products.update(products2)
print(products)

#Copy dictionary
print("-" * 60)
print("Copying two dictionaries...")
tempDict = products.copy()
tempDict.update(products2)
print(tempDict)

