from credit import *
import csv
class UserCredit:


    def __init__(self,userID):
        self.userID = userID
        self.loan_list = [] # list of object




    # def returningUser(self,):
    def add_loans(self,value,amount):
        loan = Loans(value)
        loan.setAmmount(amount)
        self.loan_list.append(loan)
    def get_loans(self):
        print("Here are loans/mortgaes for you "+self.userID+"!")
        print("Loans \t Amount\n")

        for Loans in self.loan_list:
            print(Loans.getName()+"\t $"+str(Loans.getAmmount()))
    def addtoDBase(self):
        filename = str(self.userID)+"Credit.csv"
        with open(filename,'a',newline='')as creditfile:
            creditfile.write(self.userID + ",")
            for Loans in self.loan_list:
                creditfile.write(Loans.getName()+",")
                creditfile.write(str(Loans.getAmmount())+",")
            # creditfile.write("\n")

    # def readDBase(self):
    #     with open(userID+)



def UserCL(userID,returnStatus):
    returnStatus = returnStatus
    onSystem, username = checkDB(userID)
    if (not onSystem):
        CreateLoans(username)

def CreateLoans(userID):
        user = UserCredit(userID)
        print("Seems like you have no record on file yet. Please add")
        while(True):
            loan_name = input("Enter loan name: ")
            loan_ammont = int(input("Enter Loan ammount: "))
            user.add_loans(loan_name,loan_ammont)
            continues = input("Contine? y/n: ")
            if continues == "n":
                user.get_loans()
                user.addtoDBase()
                break

def checkDB(userID):
    filename = userID+"Credit.csv"
    f = open(filename)
    for row in f:
        username = row[0:3]
    if (f.closed):
        return not (f.closed),username
    else:
        with open(filename,'r',newline='')as creditfile:
            for row in creditfile:
                col = row.split(",")


        # LOADINg user from DB
        col = col[1:]
        user = UserCredit(userID)
        print(col)
        # print(len(col)/2)
        l1 = col[0::2]
        l2 = col[1::2]
        print(l1)
        print(l2)
        for i in range(len(col)//2):
        #     if i%2 == 0:
        #
        #         # print(col[i])
            user.add_loans(l1[i],l2[i])
        #     else:
        #
        #         # print(col[i])
        #         # user.add_loans(i)
        #
        #     #

        user.get_loans()

        # print (username)
        return not (f.closed),username

# def printDB(col,username):
#
#     col = col[1:-1]
#     print(col)
#     for i in range(len(col)/2):


UserCL("Raj","S")


# user1 = UserCredit("Raj")
#
# while(True):
#     loan_name = input("ENter loan name: ")
#     loan_ammont = int(input("Enter Loan ammount: "))
#     user1.add_loans(loan_name,loan_ammont)
#     continues = input("Contine? y/n: ")
#     if continues == "n":
#         user1.get_loans()
#         user1.addtoDBase()
#         break
#
# # user1.add_loans("Car Loan",30000)
#
#
#
# user2 = UserCredit("Armaan")
#
# user2.add_loans("School",20000)
# user2.get_loans()


