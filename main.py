#SIMPLE DATA ANALYSIS FILE


from users import users
#function for simple data output
def dataPrinter(data):
    print("Name: {}, Surname: {}, age: {}, job: {}.".format(data[0], data[1], data[2], data[3]))
    
dataPrinter(users[0])
dataPrinter(users[1])
print("") #empty row

#some conditionals
if users[0][2] >= 20:
    print("Hello, {}. You are older than 20yrs.".format(users[0][0])) 
print("") #empty row

#some loop with conditionals
for x in users[1]:
    if x == "Ministar":
        print("Hello again, {}. You are politican.".format(users[1][0])) 
    if x == 55:
        print("Hello, {}. You are close to retirement.".format(users[1][0]))
