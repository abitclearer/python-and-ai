# 1. read the three side lengths
a = int(input("Side a: "))
b = int(input("Side b: "))
c = int(input("Side c: "))

# 2. any two sides together must be longer than the third one
if a + b > c and a + c > b and b + c > a:
    # an if inside an if: what kind of triangle is it?
    if a == b and b == c:
        print(f"{a}, {b}, {c}: an equilateral triangle")
    elif a == b or b == c or a == c:
        print(f"{a}, {b}, {c}: an isosceles triangle")
    else:
        print(f"{a}, {b}, {c}: a scalene triangle")
else:
    print(f"{a}, {b}, {c} can't make a triangle")

# Other runs:
# 10, 5, 3   -> 10, 5, 3 can't make a triangle
# 18, 18, 19 -> 18, 18, 19: an isosceles triangle

# Output (input: 18 | 15 | 13):
# Side a: 18
# Side b: 15
# Side c: 13
# 18, 15, 13: a scalene triangle
