from bank_accounts import *

Prosper = BankAccount(1000, 'Prosper')
Sarah = BankAccount(2000, 'Sarah')

Prosper.getBalance()
Sarah.getBalance()

Sarah.deposit(500)

Prosper.withdraw(10000)
Prosper.withdraw(10)

Prosper.transfer(10000, Sarah)
Prosper.transfer(100, Sarah)

Jim = InterestRewardsAccount(1000, 'Jim')

Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Prosper)

Blaze = SavingsAcct(1000, 'Blaze')

Blaze.getBalance()
Blaze.deposit(100)
Blaze.transfer(10000, Sarah)

Blaze.transfer(1000, Sarah)