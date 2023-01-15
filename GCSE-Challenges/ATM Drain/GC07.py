"""
GC07	
50	
ATM DRAIN	
Pooja would like to withdraw X $US from an ATM. The cash machine will only accept the transaction if X is a multiple of 5, and Pooja's account balance has enough cash to perform the withdrawal transaction (including bank charges). For each successful withdrawal the bank charges 0.50 $US. Calculate Pooja's account balance after an attempted transaction.	
"""
balance = 1000

X = int(input("Money to withdraw: "))

while X % 5 != 0 or X > balance-0.5:
  X = int(input("Money to withdraw: "))

balance -= X
balance -= 0.5
print(balance)
