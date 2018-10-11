#Write data to file
companies  = ["Microsoft", "Amazon", "Google", "Salesforce", "VMWare"]

with open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\companies.txt",'w') as companies_file:
    for company in companies:
        print(company, file=companies_file)

print("\n")
print("*" * 100)

#Read data from the recently created file.
companies_list = []
with open("C:\surajbnaik90\PythonBasics\PythonBasics\Files\companies.txt",'r') as companies_file:
    for company in companies_file:
        companies_list.append(company)  # or companies_list.append(company.strip("\n"))

print(companies_list)

for company in companies_list:
    print(company, end='')

print("\n")
print("*" * 100)