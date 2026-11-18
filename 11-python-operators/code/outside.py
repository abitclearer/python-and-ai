n = int(input("Enter a whole number: "))

# or: True when at least one side is True
print(f"{n} is outside 10 to 20:", n < 10 or n > 20)

# not flips the answer of the between check
print(f"{n} is outside 10 to 20:", not (10 <= n <= 20))

# Output (input: 56):
# Enter a whole number: 56
# 56 is outside 10 to 20: True
# 56 is outside 10 to 20: True
