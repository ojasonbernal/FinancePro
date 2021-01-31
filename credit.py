
import re
class CreditLoans:
    def __init__(self,crloans=0):
        self.crloans =crloans
    def set_crloans(self,x):
        self.crloans = x
    def add_crloans(self,x):
        self.crloans += x

class CreditCards:
    def __init__(self,name, number, exp,ccv,creditline,balance):
        self.name = name
        self.number = number
        self.exp = exp
        self.ccv = ccv
        self.creditline = int(creditline)
        self.balance = int(balance)


        moneyowed.add_crloans(balance)
        printcc = input("Do you want to print out your credit card information y/n?: ")

        if (printcc == "y" or printcc =="Y"):
            print("\n\n------Here is your credit card info-------")
            print("Card Name: "+name)

            print("Card Number: **** **** **** "+number[-4:])
            print("Card Exp: " + exp[0:2]+"/"+exp[2:4])
            print("Card CCV: " + ccv)
            print("Total Credit line: "+creditline)
            # print(creditline-balance)
            print("Total credit available: ",(self.creditline-self.balance))
            print("-------------------------------------------\n")
        else:
            print("Total credit available: ", (self.creditline - self.balance))


        # creditline = input("Enter credit line in $: ")
        # balance = input("Enter the credit balance you have left should be less credit line: ")

class Loans:
    def __init__(self,name=None):
        self.name = name
        self.amount = 0
        # self.monthly_payments
        # self.APR
    def set_name(self,x):
        self.name = x
    def setAmmount(self,ammount):
        self.amount = ammount
    def getName(self):
        return self.name
    def getAmmount(self):
        return  self.amount
    def printLoan(self):
        print("Loan name: ",self.name," $",self.amount)




def validation(data, category):#checks for credit card data validation
    num_check = False
    if (category == 1):#checks for names
        res = bool(re.search(r"\s",data))
        # for value in data:
        #     num_check = bool()
        num_check = any(map(str.isdigit,data)) #cheking for invalid name

        if ((not res) or num_check ):
            print("INVALID NAME. Please try again!")
            return False
        else:
            # print("VALID NAME")
            return True


    elif (category == 2):#checks for number
        # print(len(data))
        if((len(data) != 15) and (len(data) != 16)):
            # print(len(data))
            print("INVALID CREDIT CARD NUMBER")
            return False
        else:
            return True
    elif (category == 3): #validates exp dates
        if len(data) > 4:
            print("INVALID DATE")
            return False
        month = int(data[:2])
        year = int(data[2:4])
        # print(month)
        # print(year)
        if(month>12 or year <20):
            print("INVALID MONTH OR YEAR")
            return False
        else:
            return True

    elif(category == 4):#checks ccv validation
        if(len(data) != 3):
            print(len(data))
            print("INVALID CCV")
            return False
        else:
            return True


# credit1 = CreditCards("john", 123, 1020, 234)
##############################################################################################

moneyowed = CreditLoans()
moneyowed.set_crloans(0)

def SetCreditCards():
    print("Howdy!")

    check = False
    while (not check):
        name = input("Enter you card name: ")
        check = validation(name,1)
        # print(check)
        if(check):
            break

    check = False
    while (not check):
        number = str(input("Enter you card number: "))
        check = validation(number,2)
        if(check):
            break

    check = False
    while(not check):
        exp = (input("Enter expr month and date in the form MMYY: "))
        check = validation(exp,3)
        if (check):
            break

    check = False
    while(not check):
        ccv = (input("Enter CCV: "))
        check = validation(ccv, 4)
        if (check):
            break

    creditline = input("Enter credit line in $: ")
    balance = input("Enter the credit balance you have left, should be less than credit line: ")
    credit1 = CreditCards(name,number,exp,ccv,creditline,balance)

    loanCheck=input("Do you have any loans/mortgages y/n?: ")

    while(loanCheck == "y" or loanCheck =="Y"):
        Loans







