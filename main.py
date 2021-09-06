# Import Python Modules
import os
import json
space = ' '*71
log = False
# Creating home function

# Visit Shop --> where users can see products in the shop
def visitShop(userId):
    os.system('cls')
    # purchasedItems = {userId : {sn: {itemID:'', purchaseQuantity: ''}}}

    if userId == False:
        print('You are not login. ')
        print('You Must be logged In to View Shop')
        print('S. Sign Up')
        print('L. Log In')
        ch = input('Enter  Your Choice: ')
        if  ch == 'S' or ch == 's':
            createAccount()
            userChoice()
            os.system('pause')
            
        elif ch == 'L' or ch == 'l':
            log = login()
        # os.system('pause')
            uR = open('userRecords.json','r')
            txt = json.load(uR)       #read json object as dictionary
            uR.close()

            for i in txt:
                if log == i:
                    shop(i)                
    else:
        shop(userId)

def shop(userId):
    user = {}
    user[userId] = {}

    def addToCart(snId, itemId, qty):
        # Store snId, itemID, and qtq in user's Cart
        user[userId][snID] = {}
        user[userId][snID]['itemID'] = itemID
        user[userId][snID]['qty'] = qty
        
        # convert "user" dictionary to string so it can be add in user's Cart
        records = json.dumps(user)
        # Add user's purchased items to user's cart
        fd = open('cart.json','w')
        fd.write(records)
        fd.close()

        # if item is  added in cart then reduce it from shop and update item in particular dic
        data[itemID]['inStock'] -=  qty       
        # convert data dictionary to string to store in shop.json file
        newData = json.dumps(data)
        # Add newData to shop.json
        fd = open('shop.json','w')
        fd.write(newData)
        fd.close()
        # print message to user
        print(f'{qty} of {data[itemID]["pName"]} is Added Successfully to Cart')


    ch = 'y'
    snID = 0
    while ch == 'y' or ch == 'Y':
        os.system('cls')
        print(f'{space}Hi {userId}, Start Your Shoping:  ')
        # open shop.json in read mode so that all the data can be fetched form shop
        uR = open('shop.json','r')
        data = json.load(uR)       #read json object as dictionary
        uR.close()  
        
        # display all the details of the items present in our shop
        print('-'*120,'\n')
        print(f'  Product ID\t|  Name \t | Unit Price \t|  In Stock \t| ManufacturingDate  \t| Category \t| Description\t')
        print('-'*120,'\n')
        for id in data:
            name = data[id]['pName']
            unitPrice = data[id]['unitPrice']
            inStock = data[id]['inStock']
            manufacturingDate = data[id]['manufacturingDate']
            category = data[id]['category']
            description = data[id]['description']
            print(f' \t{id} \t| {name} \t | \t{unitPrice} \t| \t{inStock} \t| \t{manufacturingDate} \t| {category} \t| {description}\t')
        print('-'*120)
        # ask  user to enter product id
        print()
        itemID = input("Enter a Product ID You Want To Purchase: ")
        # check user enterd item is present in shop or not
        if itemID in data:
            # ask of qty 
            qty = int(input("Quantity: "))
            # store available stock in  availableStock  variable
            availableStock = data[itemID]['inStock']

            # Checking if required qty is available or not
            if qty > availableStock:
                print("Out of Stock!!! ")
                print()
                availQty = input(f"Do you want to purchase {availableStock} Quantity (Y/N): ")
                # ask user if he want to purchase available items or not
                if availQty == 'y' or availQty == 'Y':
                    qty = availableStock
                    snID += 1       #To increment Symbol number 
                    # call addToCart function which can add user's purchesed items to cart and update shop
                    addToCart(snID, itemID, qty)

                elif availQty == 'n' or availQty == 'N':
                    print()
                    print("It will be available after 5 days")
                    print()

                else:
                    print("Invalid")
            # if required qty is available then add to cart and update shop
            else:
                snID += 1       #To increment Symbol number 
                addToCart(snID, itemID, qty)
        # if user enter item id is not found then 
        else:
            print("Product ID Does Not Found")

        # after asking item id and checking again ask user if he want to purchase more items
        print()
        temp = input('Press Y to Continue Shoping  or press n to Pay Bill: ')
        print()
        if temp == 'y' or temp == 'Y':
            ch = 'Y'
        elif temp == 'n' or temp == 'N':
            logedIn()
            userChoice(userId)
            break
        else:
            print()
            print('Invalid Click... ')
            print()
            os.system('pause')
            ch == 'y'
            # break

def checkLogin(Id, Pass):
    uR = open('userRecords.json','r')
    data = json.load(uR)       #read json object as dictionary
    uR.close()

    for i in data:
        if Id == i and Pass == data[Id]["password"]:
            print('Login Successfull')
            os.system('pause')
            return True

def logedIn():
    os.system('cls')
    # os.system('hi')
    print(' '*50,'*'*50)
    print(' '*65,"--WELCOME TO THE STORE--")
    print(' '*50,'*'*50)
    print(f"{space}V. VISIT SHOP")
    print(f"{space}P. PROFILE")
    print(f"{space}C. Cart")
    print(f"{space}H. HELP")
    print(f"{space}E. EXIT")
    
def lLogedOut():
    os.system('cls')

    # os.system('hi')
    print(' '*50,'*'*50)
    print(' '*65,"--WELCOME TO THE STORE--")
    print(' '*50,'*'*50)
    print(f"{space}V. VISIT SHOP")
    print(f"{space}S. SIGN UP")
    # print(f"{space}4. Cart")
    print(f"{space}L. Login")
    print(f"{space}H. HELP")
    print(f"{space}E. EXIT")
    print(' '*50,'*'*50)
    print()
    
# User's Profile
def profile(userId):
    os.system('cls')
    uR = open('userRecords.json','r')
    data = json.load(uR)       #read json object as dictionary
    uR.close()

    # userId = '10002'
    name = data[userId]['name']
    email = data[userId]['email']
    password = data[userId]['password']
    dob = ''
    city = ''
    pin = ''
    street = ''
    mobile = ''
    print(f'Hi! {name}, You have not completed your profile yet.')

    print(f"Name        : {name}")
    print(f"DOB         : {dob}")
    # print(f"Contact : ")
    print(f"Email       : {email}")
    print(f"mobile      : {mobile}")
    # print(f"Address : ")
    print(f'City        : {city}')
    print(f'Pin Code    : {pin}')
    print(f'street      : {street}')
    print(f"Password    : {password}")

    
    print()
    print()
    os.system('pause')
    # logedIn()
    logedIn()
    os.system('pause')
    
    # return True

# Creating New Account
def createAccount(): 
    os.system('cls')
    print(f"{space}Create Your Account")
    print()
    userName = input("Name: ")
    userEmail = input("Email: ")
    userPassword = input("Password: ")
    save = input("Press S to Submit or N to Go Back: ")

    if save == "S" or save =='s':
        # userId = 10001
        uR = open('userRecords.json','r')
        data = json.load(uR)       #read json object as dictionary
        uR.close()

        # Auto Create/Increase userID
        id = int(list(data)[-1])       #Last key in a dictionar which is string so, typecast into int
        id += 1                 # increase id by 1

        # add user's detaile to userInfo dictionary
        userInfo = {}
        userInfo['name'] = userName
        userInfo['email'] = userEmail
        userInfo['password'] = userPassword

        # add user info as a value to new key in data dictionary which is fetched from json file. 
        data[id] = userInfo

        # Convert Dictionary to string so that it can be stored in json file
        newUserDetails = json.dumps(data)

        # Create or open json file in write mode
        userRecords = open('userRecords.json','w')
        userRecords.write(newUserDetails)
        userRecords.close()

        
        identity = open('userRecords.json','r')
        datas = json.load(identity)       #read json object as dictionary
        identity.close()
        
        id = list(datas)[-1]            #it return string 

        # print('id type',type(id))
        
        print(f'Hi! {userName}, Your Account Has Been Successfully Created. Please Note Your Id Number "{id}" for Login ')
        print()
        os.system('pause')
        profile(id)
        # logedIn()
        # userChoice()

        # visitShop(id)

    elif save == 'n' or  save == 'N':
        lLogedOut()
    else: 
        print("Invalid Entry: ")
        os.system('pause')
        lLogedOut()
    
def login():
    os.system('cls')
    print("WELCOME TO SIGN IN PAGE")
    Id = input("Userid: ")
    Pass = input("Password: ")
    Sub = input("PRESS S TO SUBMIT: ")

    if Sub == 'S' or Sub == 's':
        yes = checkLogin(Id, Pass)
        if yes == True:
            # profile(Id)
            # visitShop(success, Id)
            return Id
            
                

# Shoping Cart where user can see their shoping items
def Cart(userId):
    os.system('cls')
    fd = open('cart.json','r')
    data = json.load(fd)
    fd.close()

    shop = open('shop.json','r')
    text = json.load(shop)
    shop.close()
    
    totalPurchasedItem = list(data[userId])
    netTotal = 0
    # print(totalPurchasedItem)
    print('You Have Purchased: ')
    print()
    print('-'*100)
    print('Product Id \t | Product Name \t | Quantity \t | Unit Price \t | Total Price')
    print('-'*100)
    for i in totalPurchasedItem:
        # print(totalPurchasedItem)
        # print(i)
        productId = data[userId][i]['itemID']
        productName = text[productId]['pName']
        qty = data[userId][i]['qty']
        unitPrice = text[productId]['unitPrice']
        total = (qty * unitPrice)
        # print()
        print(f'  {productId} \t\t | {productName} \t\t | {qty} \t\t | {unitPrice} \t\t | {total}')
        netTotal += total
    # for i in  data['sanjay']:
    #     print(i)
    # print()
    print('-'*100)
    print(f'{space}Total = {netTotal}')
    print('-'*100)
    print()
    os.system('pause')
    # logedIn()

def help():
    print("This is help..")

# Pay the bill 
def checkout():
    print("Checkout")

# Creating dictionary for user where user information is stored such as name, email, password and so on.
# userRecord = {}

def userChoice(log):
    choice = True


    while choice == True:
        choice = input(f"{space}Enter your choice: ")

        if choice == 'V' or choice == 'v':
            os.system('cls')
            visitShop(log)
            os.system("pause")
            lLogedOut()

        elif choice == 'P' or choice == 'p':
            uR = open('userRecords.json','r')
            txt = json.load(uR)       #read json object as dictionary
            uR.close()

            for i in txt:
                if log == i:
            # if  log == True:
                # os.system('cls')
                    profile(log)
            else:
                print('You  are  not login')
                os.system("pause")
                lLogedOut()
                

        elif choice == 'S' or choice == 's':
            createAccount()
            
            # os.system("pause")

        elif choice == 'C' or choice == 'c':
            uR = open('cart.json','r')
            txt = json.load(uR)       #read json object as dictionary
            uR.close()
            # print(txt)
            for i in txt:
                # print(i)
                # print(log)
                if log == False:
                    # Cart(log)
                    print('You  are  not login')
                    os.system('pause')
                    lLogedOut()
                    break
                elif log == i:
                    Cart(log)
                    logedIn()
                    # choice = True
                    break
                elif log != i:
                    print('you have not purchased any thing')
            # else:
                # choice = True
                # print('You  are  not login')
                # print(log)
                # os.system("pause")
                
            choice = True

        elif choice == 'H' or choice == 'h':
            os.system('cls')
            help()
            os.system("pause")
            lLogedOut()

        elif choice == 'E' or choice == 'e':
            break

        elif choice == 'L' or choice == 'l':
            os.system('cls')
            log = login()
            # os.system("pause")
            logedIn()
            choice = True

        # 
        else:

            print('invalid')
            os.system('pause')
        choice = True

lLogedOut()
userChoice(log)