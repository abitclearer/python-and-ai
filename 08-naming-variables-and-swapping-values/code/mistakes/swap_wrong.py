# This file has a bug on purpose: the 10 is overwritten before it is saved, so both values end up as 20.
a = 10
b = 20

a = b
b = a
print(a, b)

# Output:
# 20 20
