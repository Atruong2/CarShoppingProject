# Jennifer, Karlee, Amy
# Car Shopping Project

def pickCar():

    make = ""
    model = ""
    option = ""
    price = ""

    def pickOption(baseprice):
        options = int(input("""You can upgrade your vehicle:\n1) Standard -- (base price)\n2) Sports -- + $3,000
              \n3) Luxury -- + $6,000\n"""))
        if (options == 1):
            option = "Standard"
            price = baseprice
            return option, price

        elif (options == 2):
            option = "Sports"
            price = baseprice + 3000
            return option, price

        elif (options == 3):
            option = "Luxury"
            price = baseprice + 6000
            return option, price



    userMake = int(input("""Please choose a make:\n1) Ford\n2) Chevrolet\n3) Toyota\n"""))
    if (userMake == 1):
        make = "Ford"
        fordModel = int(input("""Please choose a model:\n1) F-150\n2) Focus\n3) Mustang\n"""))


        if (fordModel == 1):
            model = "F-150"
            f150Baseprice = 27380
            print("The base price of a 2018 Ford F-150 is: $27,380")
            option, price = pickOption(f150Baseprice)

        elif (fordModel == 2):
            model = "Focus"
            focusBaseprice = 17860
            print("The base price of a 2018 Ford Focus is: $17,860")
            option, price = pickOption(focusBaseprice)

        elif (fordModel == 3):
            model = "Mustang"
            mustangBaseprice = 25585
            print("The base price of a 2018 Ford Mustang is: $25,585")
            option, price = pickOption(mustangBaseprice)


    print("Congrats! You've picked a " +make, model, option, "for " + str(price))
    fileHandle = open("customer.txt", "a")
    fileHandle.write("%s, %s, %s, for %s\n"%(make, model, option, price))
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