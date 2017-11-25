# Jennifer, Karlee, Amy
# Car Shopping Project

def pickCar():
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
            print("The base price of a 2018 Ford F-150 is: $27,380")
            f150Options = int(input("""You can upgrade your F-150.\n1) Standard XL -- (base price)\n2) Lariat -- $40,685
                \n3) King Ranch -- $51,600\n"""))
            if (f150Options == 1):
                option = "Standard XL"
                price = "$27,380"
            elif (f150Options == 2):
                pass
            elif (f150Options == 3):
                pass
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


    print("Congrats! You've picked a " +make, model, option, "for " + price)
    fileHandle = open("customer.txt", "a")
    fileHandle.write("%s,%s,%s, for %s\n"%(make, model, option, price))
    fileHandle.close()

def main():
    try:
        fileHandle = open("customer.txt", "r")
        lineList = fileHandle.readlines()
        print("Customer: " + lineList[len(lineList)-1])
        fileHandle.close()

    except IOError as errorMsg:
        open("customer.txt", "w")
        print("Creating new customer file...")
    finally:
        name = input("Please enter your full name!\n")
        fileHandle = open("customer.txt", "a")

        fileHandle.write(name)
        fileHandle.write(" brought a new ")
        fileHandle.close()
        pickCar()

main()