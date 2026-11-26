# the same sum with a step: start at 1 and add 2 each time, so only odd numbers come out
total = 0

for i in range(1, 101, 2):  # 1, 3, 5, ..., 99
    total += i

print("Sum of odd numbers from 1 to 100:", total)

# Output:
# Sum of odd numbers from 1 to 100: 2500
