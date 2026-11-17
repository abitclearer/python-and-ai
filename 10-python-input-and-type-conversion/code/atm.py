balance = 1000

# Step 1: ask for the PIN
pin = input("Enter your PIN: ")
print("PIN received.")

# Step 2: ask how much to take out
amount = input("How much would you like to withdraw? ")

# Step 3: show the new balance
print(f"Your new balance is {balance - int(amount)} dollars.")

# Output (input: 1234 | 200):
# Enter your PIN: 1234
# PIN received.
# How much would you like to withdraw? 200
# Your new balance is 800 dollars.
