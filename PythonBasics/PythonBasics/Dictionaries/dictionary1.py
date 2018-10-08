#Dictionary usage

#Create a dictionary object.
products = {"Microsoft" : "Cloud computing platform - Azure ",
            "Amazon": "Amazon Web Services (AWS)",
            "Google": "Google Cloud Platform (GCP)"}
backupProducts = products

#print(products)
print(products["Amazon"])

#Add item to a dictionary
products["VMware"] = "VMware cloud"
print(products)

#Update item value in the dictionary
products["Amazon"] = "AWS Cloud"
print(products)

#Delete an item from the dictionary
del products["VMware"]
print(products)

#Delete an entire dictionary
del backupProducts
#print(products) - Will throw an error as 'products' no longer exists.

#Clear the dictionary
products.clear()
print(products)

#Access the key which doesn't exist
products = {"Microsoft" : "Cloud computing platform - Azure ",
            "Amazon": "Amazon Web Services (AWS)",
            "Google": "Google Cloud Platform (GCP)"}

#print(products["Salesforce"]) - Will throw an error as 'Salesforce' key doesn't exist.