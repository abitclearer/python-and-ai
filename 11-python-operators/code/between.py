n = int(input("Enter a whole number: "))

# and: True only when both sides are True
print(f"{n} is between 10 and 20:", n >= 10 and n <= 20)

# the same check, simplified by PyCharm
print(f"{n} is between 10 and 20:", 10 <= n <= 20)

# Output (input: 15):
# Enter a whole number: 15
# 15 is between 10 and 20: True
# 15 is between 10 and 20: True
