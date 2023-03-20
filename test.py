from Transaction import *
from BankAccount import * 

#trans1 = Transaction()
#print(trans1.getAmount())
#print(trans1.getDate())

bank1 = BankAccount()
print(bank1.__str__())

bank1.deposit()
bank1.deposit()

print(bank1.__str__())
#print(bank2.getAccountNum())
