from Transaction import * 

class BankAccount: 

    # global variables used throughout the program
    OVERDRAFT_FEE = 20.00
    INTEREST_RATE = 0.075
    _accountNumber = 1000

    # constructor to make the actual bank account
    def __init__(self, firstName = "", lastName = "", balance = 0):

        # ***** handles the first name ***** 
        # if name isnt given, set the name 
        if(firstName == ""):
            self.setFirstName()

        # if it is given check the name for format
        else:
        # checks if valid length of the name 
            if(len(firstName) > 25):
                self.setFirstName()

            # checks for special characters in name 
            specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
            for char in specChars: 
                if(char in firstName):
                    self.setFirstName()
       
            self._firstName = firstName

        # ***** handles the last name ***** 
        # if name isnt given, set the name 
        if(lastName == ""):
            self.setLastName()

        else:
        # checks if valid length of the name 
            if(len(lastName) > 40):
                self.setLastName()

            # checks for special characters in name 
            specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
            for char in specChars: 
                if(char in lastName):
                    self.setLastName()
            
            self._lastName = lastName

        # ***** handles account number *****
        self._accountNum = BankAccount._accountNumber
        BankAccount._accountNumber = BankAccount._accountNumber + 1

        # ***** handles the transactions *****
        transactions = []
        self._transactions = transactions

        # ***** handles the overdrawn count of the account *****
        overdraw = 0
        self._overdrawNum = overdraw

        # ***** handles the balance ***** 
        self._balance = balance 

    
    def deposit(self):
        trans = Transaction(1)
        
        self._balance = self._balance + trans.getAmount()
        self._transactions.append(trans)


    def interest(self):
        trans = Transaction(3)

        balance = self._balance
        self._interestDeposit = BankAccount.INTEREST_RATE * balance

        self._balance = self._balance + self._interestDeposit
        self._transactions.append(trans)


    def withdrawal(self): 
        trans = Transaction(2)

        if(trans.getAmount() > self._balance + 250):
            print("Transaction is denied")
            return False
        
        elif(self._balance > 0):
            self._transactions.append(trans)
            self._balance = self._balance - trans.getAmount()
            
            if(self._balance < 0):
                self._overdrawNum = self._overdrawNum + 1
                penaltyTrans = Transaction(2, BankAccount.OVERDRAFT_FEE)
                self._balance = self._balance - BankAccount.OVERDRAFT_FEE
                print("Account is overdrawn.")
                self._transactions.append(trans)
                return False
            
            return True


   # def transfer(self, otherAccount):
     #   trans = Transaction(4)

    #    if(otherAccount.withdrawal() == True):
    #        transAmount = otherAccount.withdrawl()
     #       self._balance = self._balance + transAmount
#        elif()




    def setFirstName(self):
    
        firstName = input("Enter the first name of the account: ")

        if(firstName == ""):
            self.setFirstName()

        # if it is given check the name for format
        else:
        # checks if valid length of the name 
            if(len(firstName) > 25):
                self.setFirstName()

            # checks for special characters in name 
            specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
            for char in specChars: 
                if(char in firstName):
                    self.setFirstName()
       
            self._firstName = firstName


    def setLastName(self):

        lastName = input("Enter the last name of the account: ")

        if(lastName == ""):
            self.setLastName()

        else:
            # checks if valid length of the name 
            if(len(lastName) > 40):
                self.setLastName()

            # checks for special characters in name 
            specChars = '[@_!#$%^&*()<>?/\|}{"~:]'
            for char in specChars: 
                if(char in lastName):
                    self.setLastName()
        
            self._lastName = lastName


    def setAccountNum(self):
        pass

    def setTransactions(self):
        pass

    def setOverdrawCount(self):
        pass

    def setBalance(self):
        pass

    def getFirstName(self):
        return self._firstName

    def getLastName(self):
        return self._lastName

    def getAccountNum(self):
        return self._accountNum

    def showTransactions(self):

       # for item in self._transactions 
            
        return 0

    #def getOverdrawCount(self):
        #return self._overdrawNum

    #def getBalance(self):
        #return self._balance 
    
    # Prints all of the transaction instance variables.
    # @return: The formatted, human readable string of the transaction
    def __str__ (self):
        transaction = []
        for item in self._transactions:
            transaction.append(item) 

        return ("Account Details - First Name: %s, Last Name: %s, Account Number: %d, Balance: $%.2f, Transactions: %s"\
                 %(self._firstName, self._lastName, self._accountNum, self._balance, transaction))
    

    # Prints all of the transaction instance variables.
    # @return: The formatted, machine readable string of the transaction
    def __repr__ (self):
        return ("Transaction(tNumber = %d, amount = $%.2f, date = %s, tType = %s)" %(self._tNumber, self._amount, self._date, self._tType))
