# Jennifer, Karlee, Amy
# Car Shopping Project

def pickCar():

    make = ""
    model = ""
    option = ""
    price = 0.00

    # Return the price and option of a car picked:
    def pickOption(baseprice):

        options = int(input('''
        You can upgrade your vehicle:
        1) Standard -- + $0.00
        2) Sports -- + $3,000.00
        3) Luxury -- + $6,000.00
        '''))
        if (options == 1):
            option = "Standard"
            price = baseprice
            return option, price

        elif (options == 2):
            option = "Sports"
            price = baseprice + 3000.00
            return option, price

        elif (options == 3):
            option = "Luxury"
            price = baseprice + 6000.00
            return option, price

    userMake = int(input('''
    Please choose a make:
    1) Ford
    2) Chevrolet
    3) Toyota
    '''))

    # Following code gets executed if user picks Ford as a make:
    if (userMake == 1):
        make = "Ford"
        fordModel = int(input('''
        Please choose a model:
        1) F-150
        2) Focus
        3) Mustang
        '''))
        if (fordModel == 1):
            model = "F-150"
            f150Baseprice = 27380.00
            print("The base price of a 2018 Ford F-150 is: $27,380.00")
            option, price = pickOption(f150Baseprice)

        elif (fordModel == 2):
            model = "Focus"
            focusBaseprice = 17860.00
            print("The base price of a 2018 Ford Focus is: $17,860.00")
            option, price = pickOption(focusBaseprice)

        elif (fordModel == 3):
            model = "Mustang"
            mustangBaseprice = 25585.00
            print("The base price of a 2018 Ford Mustang is: $25,585.00")
            option, price = pickOption(mustangBaseprice)

    # Following code gets executed if user picks Chevrolet as a make:
    elif userMake == 2:
        make = "Chevrolet"
        chevyModel = int(input('''
        Please choose a model:
        1) Camaro
        2) Corvette Stingray
        3) Silverado
        '''))
        if (chevyModel == 1):
            model = "Camaro"
            camaroBaseprice = 25905.00
            print("The base price of a 2018 Chevy Camaro is: $25,905.00")
            option, price = pickOption(camaroBaseprice)

        elif (chevyModel == 2):
            model = "Corvette Stingray"
            corvetteBaseprice = 55495.00
            print("The base price of a 2018 Chevy Corvette Stingray is: $55,495.00")
            option, price = pickOption(corvetteBaseprice)

        elif (chevyModel == 3):
            model = "Silverado"
            silveradoBaseprice = 28085.00
            print("The base price of a 2018 Chevy Silverado is: $28,085.00")
            option, price = pickOption(silveradoBaseprice)

    # Following code gets executed if user picks Toyota as a make:
    elif (userMake == 3):
        toyotaModel = int(input('''
    Please choose a model:
    1) Highlander
    2) Camry
    3) Corolla
    '''))
        if (toyotaModel == 1):
            model = "Highlander"
            highlanderBaseprice = 31030.00
            print("The base price of a 2018 Toyota Highlander is: $31,030.00")
            option, price = pickOption(highlanderBaseprice)

        elif (toyotaModel == 2):
            model = "Camry"
            camryBaseprice = 23495.00
            print("The base price of a 2018 Toyota Camry is: $23,495.00")
            option, price = pickOption(camryBaseprice)

        elif (toyotaModel == 3):
            model = "Corolla"
            corollaBaseprice = 18550.00
            print("The base price of a 2018 Toyota Corolla is: $18,550.00")
            option, price = pickOption(corollaBaseprice)

    # The :, adds a comma as a thousands separator, and the .2f limits the string to two decimal places
    # (or adds enough zeroes to get to 2 decimal places) at the end.
    price = '${:,.2f}'.format(price)

    print("Congrats! You've picked a " +make, model, option, "for " + price)
    fileHandle = open("customer.txt", "a")
    fileHandle.write("%s, %s, %s, for %s\n" %(make, model, option, price))
    fileHandle.close()

def main():
    try:
        fileHandle = open("customer.txt", "r")
        lineList = fileHandle.readlines()
        print(lineList[len(lineList)-1])
        fileHandle.close()

    except IOError as errorMsg:
        open("customer.txt", "w")
        print("Creating new customer file...")
    finally:
        print("")
        name = input("Please enter your full name!\n")
        fileHandle = open("customer.txt", "a")

        fileHandle.write(name)
        fileHandle.write(" brought a new ")
        fileHandle.close()
        pickCar()

main()