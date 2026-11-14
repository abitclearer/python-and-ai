# Swap two variables with a temporary variable
a = 10
b = 20

temp = a  # save the value of a: temp holds 10
a = b     # a is now 20
b = temp  # b gets the original 10

print(a, b)

# The Python shortcut: the right side is worked out first
a, b = b, a
print(a, b)

# Output:
# 20 10
# 10 20
