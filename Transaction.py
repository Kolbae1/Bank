
# @author John McManus
# import the datetime class used to get today's date
import datetime
# This module defines the Transaction class.
# A class to represent the data elements and methods required to implement a backaccount transaction.
class Transaction :
    _nextTransaction = 100 # A private class variable that hold the number of the next transaction
    DEBUG = True # A class constant that turns debugging printing on and off
    RESET_TNUMBER = True
    
# Constructs a transaction.
# @param tType: the type of this transaction (String: default is an empty string)
# @param amount: the amount of this transaction (Floating point: default is 0.0, must be a positive float)
# @param date: the date of the transaction (String: default is an empty string)
# @require: date is a string in the format Year-Month-Day -> "2021-03-24"
# @ensure self._amount >= 0
# @ensure date is a valid date
    def __init__(self, tType = "", amount = 0.0, date = "") :

        if Transaction.DEBUG:
            print ("Creating a new transaction")

        if Transaction.RESET_TNUMBER:
            Transaction._nextTransaction = 100
            # Set the transaction number and increment the next transaction class variable
            self._tNumber = Transaction._nextTransaction
            Transaction._nextTransaction = Transaction._nextTransaction + 1
            # if the tType is an empty string, prompt for the tType
            
        if tType == "":
            self.setTType()
        else:
            self._tType = tType

        # if the amount is 0.0, prompt for the amount
        if amount <= 0 and self._tType != 3:
            self.setAmount()
        else:
            self._amount = amount
        # if the date is an empty string, set the date to today's date
        if date == "":
            self.setDate()
        else:
            date =date.split("-")
            self._year = date[0]
            self._month = date[1]
            self._day = date[2]

        # set the date instance variable
        self._date = self._year + "-" + self._month + "-" + self._day
        return
    

    # Define the Special Methods Needed
    # Checks an transaction to see if it is equal to the second transaction.
    # @param other: the transaction your are comparing the first transaction with
    # @return result: True if this two transaction have the same amount and dates,and tNumber
    def __eq__(self, other) :
        result = (self._amount == other._amount) and (self._date == other._date) and (self._tNumber == other._tNumber)
        return result
    

    # Checks an transaction to see if it is not equal to the second transaction.
    # @param other: the transaction your are comparing the first transaction with
    # @return result: True if this two transaction have the same amount and dates, and tNumber
    def __ne__(self, other) :
        result = (self._amount != other._amount) or (self._date != other._date) or (self._tNumber != other._tNumber)
        return result
    

    # adds an transaction to the second transaction.
    # @param other: the transaction your are adding the first transaction to
    # @return result: the sum of the two transaction prices
    def __add__(self, other) :
        return (self._amount + other._amount)
    

    # adds an transaction to the second transaction.
    # @param other: the transaction your are adding the first transaction to
    # @return result: the sum of the two transaction amounts
    def __sub__(self, other) :
        return (self._amount - other._amount)
    

    # implements the sum() function that will sum a list of the Transactions
    # @param other: the transaction your are adding to the sum
    # @return: the sum of the transaction amounts in the list
    def __radd__(self, other):
        return other + self._amount
    

    # Define the accessor methods
    # getAmount returns the amount of the transaction.
    # @return: The amount of the transaction
    def getAmount(self) :
        return self._amount
    

    # getDate returns the date of the transaction.
    # @return: The date of the transaction
    def getDate(self) :
        return self._date
    

    # getTNumber returns the transaction number of the transaction.
    # @return: The transaction number of the transaction
    def getTNumber(self) :
        return self._tNumber
    

    # getTType returns the transaction type of the transaction.
    # @return: The transaction type of the transaction
    def getTType(self) :
        return self._tType
    

    # Prints all of the transaction instance variables.
    def printTransaction(self):
        print("Transaction # %d, amount $%.2f, date %s type: %s" % (self._tNumber,self._amount, self._date, self._tType))


    # Prints all of the transaction instance variables.
    # @return: The formatted, human readable string of the transaction
    def __str__ (self):
        return ("Transaction # %d, amount = $%.2f, date %s, type: %s" %(self._tNumber, self._amount, self._date, self._tType))
    

    # Prints all of the transaction instance variables.
    # @return: The formatted, machine readable string of the transaction
    def __repr__ (self):
        return ("Transaction(tNumber = %d, amount = $%.2f, date = %s, tType = %s)" %(self._tNumber, self._amount, self._date, self._tType))
    

    # Define the mutator methods
    # Mutator method that sets the transaction type for a transaction
    # @ensure tType: must be Deposit, Withdrawal, Interest, Transfer, or Penalty.
    def setTType(self):
        optionSet = {1, 2, 3, 4}
        option = None
        while option not in optionSet:
            print("Please enter the transaction type")
            print("Select from: ")
            print(" 1 - Deposit")
            print(" 2 - Withdrawl")
            print(" 3 - Interest Payment")
            print(" 3 - Transfer", end = "")
            option = int(input(":"))
            
        if option == 1:
            tType = "deposit"
        elif option == 2:
            tType = "withdrawl"
        elif option == 3:
            tType = "interest"
        elif option == 4:
            tType = "transfer"
        else:
            print("Invalid input")
            tType = None

        self._tType = tType
        return
    

    # Mutator method that sets the amount for a transaction
    # @ensure self._amount >= 0
    def setAmount(self):
        amount = int(input("Please enter an amount (positive) for the transaction:"))
        while amount < 0:
            amount = int(input("Please enter an amount (positive) for the transaction:"))

        self._amount = amount
        return
    

    # Mutator method that sets the date for a transaction
    def setDate(self):
        date = str(datetime.date.today())
        date = date.split("-")
        self._year = date[0]
        self._month = date[1]
        self._day = date[2]
        #if Transaction.DEBUG:
            #arf = self._date.split("-")
            #print(arf)
            
        return

