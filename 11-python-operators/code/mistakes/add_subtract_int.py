# This file raises an error on purpose: int() can't read a number with a decimal point. Use float() for that.
x = int(input("Enter x: "))
y = int(input("Enter y: "))
print("x + y =", x + y)
print("x - y =", x - y)

# Output (input: 0.5 | 0.4):
# Enter x: 0.5
# ValueError: invalid literal for int() with base 10: '0.5'
