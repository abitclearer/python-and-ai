print("Hello")
print(type("Hello"))  # str

print(type(10))  # int
print(type(3.14))  # float
print(type(True))  # bool
print(type(False))  # bool
print(type(None))  # NoneType

num = -100
print(type(num))
num = "Hello"
print(type(num))

num = -100
print(isinstance(num, int))  # True
print(isinstance(num, float))  # False
print(isinstance(num, bool))  # False

# Output:
# Hello
# <class 'str'>
# <class 'int'>
# <class 'float'>
# <class 'bool'>
# <class 'bool'>
# <class 'NoneType'>
# <class 'int'>
# <class 'str'>
# True
# False
# False
