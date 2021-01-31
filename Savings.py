
f = open("Savings.csv", "a", newline='')
# Check if customer has data stored already.
# If yes, retrieve data
# If no, Ask all info


def returningUser():
    """Checks to see if a returning user with previous data accesses the savings feature of the app. We then retreive the information."""
    pass


# BELOW IS FOR NEW USER ON SAVINGS DATA BASE
def newUser():
    def error_prompt_():
        while True:
            error_prompt = input('Would you like to try again? (Enter yes/no): ')
            if error_prompt.lower() != 'no' and error_prompt.lower() != 'yes':
                print('Wrong input.')
                continue
            elif error_prompt.lower() == 'no':
                loop = False
                print('Thank you and Goodbye.')
                exit()
            elif error_prompt.lower() == 'yes':
                break
            else:
                continue
    
    def savings():
        print("-----------------------------------------------------------------------------------------------------")
        print("Howdy! In order for us to help you achieve your financial goals, we need a little information on you.")
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
        f.write(str(totalCheckingbalance)+",")
    
    def optionTwo():
        while True:
            try:
                totalSavingsbalance = float(input("Enter value here: "))
                break
            except:
                print('Wrong input.')
                error_prompt_()
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
        f.write(str(totalSavingsbalance)+",")

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
        f.write(str(savingsGoal)+"\n")

    def optionFour():
        pass

    savings()

newUser()
f.close()