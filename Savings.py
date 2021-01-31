

def intro():
    print("-----------------------------------------------------------------------------------------------------")
    print("Howdy! In order for us to help you achieve your financial goals, we need a little information on you.")

def savings():
    print("-----------------------------------------------------------------------------------------------------\n")
    print("Enter total amount in checking account/s")
    optionOne()
    print("Enter total amount in saving account/s")
    optionTwo()
    print("Enter savings goals")
    optionThree()
    print("Exit to main menu")
    optionFour()


def optionOne():

    totalCheckingbalance = input("")
    print("Your Total Amount In Your Checking Account/s is: $", totalCheckingbalance)
    print("Is this correct? Y/N")
    yesOrNo = input("")
    if (yesOrNo.lower() == "n"):
        while(True):
            print("Enter total amount in checking account/s")
            totalCheckingbalance = input("")
            print("Your Total Amount In Your Checking Account/s is: $", totalCheckingbalance)
            print("Is this correct? Y/N")
            yesOrNo = input("")
            if (yesOrNo.lower() == "y"):
                break
            print("-----------------------------------------------------------------------------------------------------\n")

def optionTwo():
    totalSavingsbalance = input("")
    print("Your Total Amount In Your Savings Account/s is: $", totalSavingsbalance)
    print("Is this correct? Y/N")
    yesOrNo = input("")
    if (yesOrNo.lower() == "n"):
        while(True):
            print("Enter total amount in savings account/s")
            totalCheckingbalance = input("")
            print("Your Total Amount In Your Savings Account/s is: $", totalCheckingbalance)
            print("Is this correct? Y/N")
            yesOrNo = input("")
            if (yesOrNo.lower() == "y"):
                break
            print("-----------------------------------------------------------------------------------------------------\n")

def optionThree():
    savingsGoal = input("")
    print("Your savings goal is: $", savingsGoal)
    print("Is this correct? Y/N")
    yesOrNo = input("")
    if (yesOrNo.lower() == "n"):
        while(True):
            print("Enter total amount in checking account/s")
            totalCheckingbalance = input("")
            print("Your Total Amount In Your Checking Account/s is: $", totalCheckingbalance)
            print("Is this correct? Y/N")
            yesOrNo = input("")
            if (yesOrNo.lower() == "y"):
                break
            print("-----------------------------------------------------------------------------------------------------\n")

def optionFour():
    pass

intro()
# 

savings()
# Enter an option
# 1. Total Amount in Checking Accounts
# 2. Total Amount in Saving Accounts
# 1. Setting Financial Goal
