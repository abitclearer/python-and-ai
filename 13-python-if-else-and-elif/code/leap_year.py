# Leap year rules:
#   a year that isn't a whole century is a leap year when it divides evenly by 4
#   a century year (1900, 2000) is a leap year only when it divides evenly by 400
year = int(input("Enter a year: "))

if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is a common year")

# Other runs:
# 1900 -> 1900 is a common year
# 2004 -> 2004 is a leap year
# 2400 -> 2400 is a leap year

# Output (input: 2025):
# Enter a year: 2025
# 2025 is a common year
