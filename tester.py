from Transaction import *
from BankAccount import * 

#trans1 = Transaction()
#print(trans1.getAmount())
#print(trans1.getDate())

bank1 = BankAccount()
print(bank1.__str__())

userInput = input("Please enter what you would like to do (""d"" for deposit, ""i"" for recieving interest, ""w"" to withdrawl, ""q"" to quit): ")
while userInput != "q":
    if userInput == "d":
        bank1.deposit()
        print("Deposit made")
        userInput = input("Please enter what you would like to do (""d"" for deposit, ""i"" for recieving interest, ""w"" to withdrawl, ""q"" to quit): ")

    elif userInput == "i":
        bank1.interest()
        print("interest payment made")
        userInput = input("Please enter what you would like to do (""d"" for deposit, ""i"" for recieving interest, ""w"" to withdrawl, ""q"" to quit): ")
    elif userInput == "w":
        print("Function not yet complete.")
        userInput = input("Please enter what you would like to do (""d"" for deposit, ""i"" for recieving interest, ""w"" to withdrawl, ""q"" to quit): ")
    else:
        userInput = input("Please enter what you would like to do (""d"" for deposit, ""i"" for recieving interest, ""w"" to withdrawl, ""q"" to quit): ")

print(bank1.__str__())


#print(bank2.getAccountNum())