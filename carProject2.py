# Jennifer, Karlee, Amy
# Car Shopping Project

def pickCar():

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


    make = ""
    model = ""
    option = ""
    price = ""
    userMake = int(input("""Please choose a make:\n1) Ford\n2) Chevrolet\n3) Toyota\n"""))
    if (userMake == 1):
        make = "Ford"
        fordModel = int(input("""Please choose a model:\n1) F-150\n2) Focus\n3) Mustang\n"""))
        if (fordModel == 1):
            model = "F-150"
            f150baseprice = 27380
            print("The base price of a 2018 Ford F-150 is: $27,380")
            option, price = pickOption(f150baseprice)

        elif (fordModel == 2):
            print("The base price of a 2018 Ford Focus is: $17,860")
            focusOptions = int(input("""You can upgrade your Focus.
            1) Standard Sedan -- (base price)
            2) Titanium Sedan -- $24,175
            3) Electric -- $29,120"""))
        elif (fordModel == 3):
            print("The base price of a 2018 Ford Mustang is: $25,585")
            mustangOptions = int(input("""You can upgrade your Mustang.
            1) Standard EcoBoost -- (base price)
            2) EcoBoost Convertible -- $31,085
            3) Shelby GT350 -- $57,145"""))

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