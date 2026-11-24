# add up every even number from 1 to 100
total = 0  # the running total
i = 1  # the number the loop starts from

while i <= 100:  # <= so that 100 itself is included
    if i % 2 == 0:  # nothing left over after dividing by 2: even
        total += i
    i += 1  # move on to the next number

# not indented: runs once, after the loop is done
print(f"The sum of even numbers from 1 to 100 is {total}")

# Output:
# The sum of even numbers from 1 to 100 is 2550
