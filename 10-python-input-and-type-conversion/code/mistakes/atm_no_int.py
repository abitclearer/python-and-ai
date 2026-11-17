# This file raises an error on purpose: amount is a string, and Python can't subtract a string from a number.
balance = 1000

# Step 1: ask for the PIN
pin = input("Enter your PIN: ")
print("PIN received.")

# Step 2: ask how much to take out
amount = input("How much would you like to withdraw? ")

# Step 3: show the new balance
print(f"Your new balance is {balance - amount} dollars.")

# Output (input: 1234 | 200):
# TypeError: unsupported operand type(s) for -: 'int' and 'str'
