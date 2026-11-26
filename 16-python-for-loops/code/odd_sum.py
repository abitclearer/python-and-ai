# add up every odd number from 1 to 100
total = 0  # where the sum builds up

for i in range(1, 101):  # 1, 2, ..., 100 (the end, 101, is never included)
    if i % 2 == 1:  # 1 left over after dividing by 2: odd
        total += i

# not indented: runs once, after the loop
print("Sum of odd numbers from 1 to 100:", total)

# Output:
# Sum of odd numbers from 1 to 100: 2500
