# add up every multiple of 3 between 100 and 500
total = 0

for i in range(100, 501):  # 100, 101, ..., 500
    if i % 3 == 0:  # nothing left over after dividing by 3
        total += i

print("Sum of multiples of 3 from 100 to 500:", total)

# Output:
# Sum of multiples of 3 from 100 to 500: 39900
