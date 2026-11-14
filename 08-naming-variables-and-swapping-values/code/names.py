# Identifier rules: letters, digits and underscores; no digit first; no keywords; case sensitive
true = 1  # lowercase true is not a keyword, so it is a legal name
print(true)

name6 = "Python"  # a digit is fine, just not at the start
print(name6)

age = 1
Age = 2
AGE = 3  # three different variables
print(age, Age, AGE)

# Output:
# 1
# Python
# 1 2 3
