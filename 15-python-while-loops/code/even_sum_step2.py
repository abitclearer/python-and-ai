# another way: start at 2 and add 2 each time, so every i is even
total = 0
i = 2

while i <= 100:
    total += i
    i += 2

print(f"The sum of even numbers from 1 to 100 is {total}")

# Output:
# The sum of even numbers from 1 to 100 is 2550
