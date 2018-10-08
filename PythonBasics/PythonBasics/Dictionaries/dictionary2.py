products = {"Microsoft" : "Cloud computing platform - Azure ",
            "Amazon": "Amazon Web Services (AWS)",
            "Google": "Google Cloud Platform (GCP)"}
print(products)

while True:
    dict_key = input("Please enter the company name: ")
    if dict_key == "quit":
        break
    if dict_key in products:
        cloudProviderName = products.get(dict_key)
        print("Cloud Provider name is {}".format(cloudProviderName))
    else:
        print("Company name '{}' doesn't exist in our list".format(dict_key))



