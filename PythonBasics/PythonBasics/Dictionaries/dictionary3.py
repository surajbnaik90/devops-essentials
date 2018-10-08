products = {"Microsoft" : "Cloud computing platform - Azure ",
            "Amazon": "Amazon Web Services (AWS)",
            "Google": "Google Cloud Platform (GCP)"}
print(products)

while True:
    dict_key = input("Please enter the company name: ")
    if dict_key == "quit":
        break
    description = products.get(dict_key,"Company name '{}' doesn't exist in our list".format(dict_key))
    print(description)
    break


#List out all cloud provider names
for name in products:       
    print(products[name])
    
#Important point: There is no guarantee that items will
#appear in the same order in the dictionary. Keep running for few times, result will be different. 
#Tried on - IntelliJ IDEA tool. 
for i in range(10):
    for name in products:
        print(products[name])
    print("-" * 60)


#Sort the dictionary keys:
for company in sorted(products.keys()):
    print(products[company])


#Notes
print(products.keys())
print(products.values())