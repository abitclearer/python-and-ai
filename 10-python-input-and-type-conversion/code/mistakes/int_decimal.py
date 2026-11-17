# This file raises an error on purpose: int can't read a decimal number written as text. Use float for that.
print(int("3.5"))

# Output:
# ValueError: invalid literal for int() with base 10: '3.5'
