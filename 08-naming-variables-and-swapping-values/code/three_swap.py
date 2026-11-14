# Three-way swap: a's value goes into c, b's into a, c's into b
a = 100
b = 200
c = 300

temp = a
a = b
b = c
c = temp
print(a, b, c)

# The same in one line
a, b, c = 100, 200, 300
a, b, c = b, c, a
print(a, b, c)

# Output:
# 200 300 100
# 200 300 100
