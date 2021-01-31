class User:

    def __init__(self, name, dob, ssn, i_d, account_num, email, password):
        self.name = name
        self.dob = dob
        self.ssn = ssn
        self.i_d = i_d
        self.account_num = account_num
        self.email = email
        self.password = password
        self.creditScore = 0
        self.CreditLoans = 0


    def getName(self):
        return  self.name
    def getDOB(self):
        return  self.dob
    def getSSN(self):
        return  self.ssn
    def getID(self):
        return self.i_d
    def getACCTNUM(self):
        return self.account_num
    def getEmail(self):
        return self.email
    def getPSSW(self):
        return  self.password

    def setCreditScore(self,score):
        self.creditScore = score
    def setCreditloans(self, loan):
        self.creditLoans = loan
