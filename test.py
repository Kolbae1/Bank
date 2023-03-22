from Transaction import *
from BankAccount import * 

#trans1 = Transaction()
#print(trans1.getAmount())
#print(trans1.getDate())

bank1 = BankAccount()
bank2 = BankAccount()

bank1.deposit()
bank2.deposit()

print(bank1.__str__())
print(bank2.__str__())


bank1.transfer(bank2)

#bank1.interest()

print(bank1.__str__())
print("")
print(bank1.getBalance())
