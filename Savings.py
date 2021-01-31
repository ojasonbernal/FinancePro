import math

def intro():
    print("Howdy! In order for us to help you achieve your financial goals, we need a little information on you.")

def options():
    print("Choose one of the following options below:")
    print("1. Enter total amount in checking accounts")
    print("2. Enter total amount in saving accounts")
    print("3. Enter savings goals")
    print("4. Exit to main menu")

def savings():
    options()
    option = input("")  # Default a string
    if option == "1":
        optionOne()
    elif option == "2":
        optionTwo()
    elif option == "3":
        optionThree()
    elif option == "4":
        optionFour()
    else:
        print("Invalid command. Try again.")
        
def verification(boolValue):
    while(not boolValue): 
        print("Invalid command. Try again.")


def optionOne():
    print("-----------------------------------------------------\n")
    print("How many checking accounts do you have?")
    amountOfcheckingAccounts = input("")

    verification(amountOfcheckingAccounts.isdigit)

    totalCheckingbalance = 0
    if(amountOfcheckingAccounts.isdigit):
        for i in range(0,int(amountOfcheckingAccounts)):
            print("Enter amount for Account #" + str(i))
            balance = input("")
            verification(balance.isfloat or balance.isdigit)
            totalCheckingbalance += float(balance)


def optionTwo():
    pass

def optionThree():
    pass

def optionFour():
    pass

intro()
savings()
# Enter an option
# 1. Total Amount in Checking Accounts
# 2. Total Amount in Saving Accounts
# 1. Setting Financial Goal
