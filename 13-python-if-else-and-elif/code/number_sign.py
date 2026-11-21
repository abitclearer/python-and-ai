# positive, negative or zero: Python checks from top to bottom,
# and only the first condition that is True runs its block
number = int(input("Enter a number: "))

if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print("It's zero")

# Other runs:
# -1 -> -1 is negative
# 0  -> It's zero

# Output (input: 5):
# Enter a number: 5
# 5 is positive
