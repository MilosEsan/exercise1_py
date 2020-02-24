#simple data
user1 = ("Shommy", "Em", 29, "Junior Developer")
user2 = ("Mirko", "Mirkovic", 55, "Ministar")
#function for simple data output
def dataPrinter(data):
    formatString ="Name: %s, Surname: %s, age: %s, job: %s."
    print(formatString % data)

dataPrinter(user1)
dataPrinter(user2)
print("") #empty row

#some conditionals
if user1[2] >= 20:
    print("Hello, %s. You are older than 20yrs." % user1[0]) 
print("") #empty row

#some loop with conditionals
for x in user2:
    if x == "Ministar":
        print("Hello again, %s. You are politican." % user2[0]) 
    if x == 55:
        print("Hello, %s. You are close to retirement." % user2[0])
