from easygui import *

image1 = "/Users/My_Mac/Desktop/database/logo.gif"
#Check strings
def stringValidation(aString):
    valid = aString.isalpha()
    if valid:
        return True

    else:
        return False


#Check Ints
def intValidation(aInt):
    valid = aInt.isdigit()
    if valid:
        return True

    else:
        return False

#Check phone Num Length
def phoneValidation(aPhoneNumber):
    if len(aPhoneNumber) == 11:
        return True
    else:
        return False

def passwordMenu():
    chances = 3
    guess = passwordbox("Enter your password", "Password","learn2code", image1, root=None)

    while guess!= "learn2code":
        
        print("Wrong Password")
        chances = chances - 1
        if chances == 0:
            print("NO MORE CHANCES")
            exit()
        
        guess = passwordbox("Password Invalid! Try Again", "Password","", image1, root=None)

    mainMenu()

def mainMenu():
    choice = ["Add Customer","Add Product","Add Order","View Customers","View Products","View Orders","Run Customer Query","Exit"]
    buttonChoice = buttonbox("Main Menu", "Main Menu", choice, image1)

    if buttonChoice == "Add Customer":
        addCustomer()

    elif buttonChoice == "View Customers":
        viewCustomer()
        
    elif buttonChoice == "Add Product":
        addProduct()

    elif buttonChoice == "View Products":
        viewProducts()

    elif buttonChoice == "Add Order":
        addOrder(image1)
        
    elif buttonChoice == "View Orders":
        viewOrders()
        
    elif buttonChoice == "Run Customer Query":
        customerQuery()
        
    else:
        exitCheck()
        
def addCustomer():
    fieldNames = ["First Name", "Surname", "County", "Phone Number"]
    customerData = multenterbox("Add Customer","Enter the customer data below",fieldNames,["","","","07"])

    if customerData == None:
        mainMenu()

    else:

        fNameCheck = stringValidation(customerData[0])
        sNameCheck = stringValidation(customerData[1])
        countyCheck = stringValidation(customerData[2])
        phoneIntCheck = intValidation(customerData[3])
        phoneLenCheck = phoneValidation(customerData[3])

        print(fNameCheck)
        print(sNameCheck)
        print(countyCheck)
        print(phoneIntCheck)
        print(phoneLenCheck)

        if fNameCheck != True or sNameCheck != True or countyCheck != True or phoneIntCheck != True or phoneLenCheck != True:
            msgbox("Invalid Entry. Check your Data and re-enter the Customer Details")
            addCustomer()

        else:
            
        
            file = open("customerNumber.txt","r")
            customerNumber = file.read()
            file.close()

            file = open("customerNumber.txt","w")
            newNum = int(customerNumber)+1
            file.write(str(newNum))
            file.close()

            
            
            file = open("customers.txt","a+")

            file.write(str(customerNumber)+",")

            for x in range(0, len(customerData)):
                file.write(customerData[x]+",")

            file.write("\n")
            file.close()
            mainMenu()


   
def addProduct():
    fieldNames = ["ID", "Product Names", "Quantity in Stock", "Manufacturer"]
    productData = multenterbox("Add Customer", "Enter the customer data below", fieldNames, ["0","","0",""])

    if productData == None:
        mainMenu()

    else:
        idCheck = intValidation(productData[0])
        productNameCheck = stringValidation(productData[1])
        quantityCheck = intValidation(productData[2])
        manufacturerCheck = stringValidation(productData[3])

        print(idCheck)
        print(productNameCheck)
        print(quantityCheck)
        print(manufacturerCheck)

        if idCheck != True or productNameCheck != True or quantityCheck != True or manufacturerCheck != True:
            msgbox("Invalid Entry, Check product details and try again...")
            addProduct()

        else:
            
            file = open("products.txt","a+")

            for x in range(len(productData)):
                file.write(productData[x]+",")

            file.write("\n")
            file.close()
            mainMenu()







        

def addOrder(image):
    ID = enterbox("Enter the Id of the Customer", "Customer ID", "0")

    #Find amount of lines
    file = open("customers.txt", "r")
    length = len(file.readlines())
    file.close()

    #check File
    file = open("customers.txt", "r")

    for x in range(0, length):
        line = file.readline()
        customerLine = line.split(",")
        if ID == customerLine[0]:
            customer = customerLine
            break
        else:
            customer = ""

    file.close()

    if customer == "":
        msgbox("Customer not found!", "Not Found", "OK", image, root = None)
        mainMenu()

    else:
        message = "Did you mean: " + customerLine[1] + customerLine[2]
        check = ynbox(message, "Customer Check")
        if check == False:
            mainMenu()

        else:
            #Find amount of lines
            file = open("products.txt", "r")
            length = len(file.readlines())
            file.close()

            #Get The products
            file = open("products.txt", "r")
            products = []
            for x in range(0, length - 1):
                line = file.readline()
                productLine = line.split(",")
                products.append(productLine[1])
            file.close()

            choice = choicebox("Pick a product", "Product choice", products)

            if choice == None:
                mainMenu()

            else:
                quantity = enterbox("Enter the Quantity Needed:", "Quantity", "")
                if quantity == None:
                    mainMenu()

                else:
                    file = open("orderNumber.txt","r")
                    orderNumber = file.read()
                    file.close()

                    file = open("orderNumber.txt","w")
                    newNum = int(orderNumber)+1
                    file.write(str(newNum))

                    file = open("orders.txt","a+")
                    file.write(ID+","+orderNumber+","+choice+","+quantity+","+"\n")
                    file.close()
                    msgbox("Order has been added!", "Order Menu", "OK", image, root = None)
                    mainMenu()



#Queries
def customerQuery():
    ID = enterbox("Enter the Id of the Customer", "Customer ID", "")

    #Find amount of lines
    file = open("customers.txt", "r")
    length = len(file.readlines())
    file.close()

    #check File
    file = open("customers.txt", "r")

    for x in range(0, length):
        line = file.readline()
        customerLine = line.split(",")
        if ID == customerLine[0]:
            customer = customerLine
            break
        else:
            customer = ""

    file.close()

    if customer == "":
        msgbox("Customer not found!", "Not Found", "OK", image, root = None)
        mainMenu()

    else:
        message = "Did you mean: " + customerLine[1] + customerLine[2]
        check = ynbox(message, "Customer Check")
        if check == False:
            mainMenu()
        else:
            file = open("orders.txt","r")
            length = len(file.readlines())
            file.close()

            file = open("orders.txt","r")
            data = []
            for x in range (0, length):
                line = file.readline()
                if line[0] == ID:
                    data.append(line)
            message = customerLine[1] +" "+customerLine[2]

            codebox(message, "Order Query", data)
            mainMenu()
                    














                
                







                    











                
            
    
    

def viewProducts():
    file = open("products.txt", "r")
    productData = file.read()
    codebox("Product Records:", "Product Data", productData)
    file.close()
    mainMenu()

def viewOrders():
    file = open("orders.txt", "r")
    orderData = file.read()
    codebox("Order Records:", "Order Data", orderData)
    file.close()
    mainMenu()

def viewCustomer():
    file = open("customers.txt","r")
    customerData = file.read()
    codebox("Customer Records:", "Customer Data", customerData)
    file.close()
    mainMenu()


def exitCheck():
    exitChoice = ynbox("Are you sure you want to quit?", "Quit Checker")

    if exitChoice == True:
        exit()

    else:
        mainMenu()



passwordMenu()










    
