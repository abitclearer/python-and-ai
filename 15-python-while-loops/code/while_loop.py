# print the same line ten times with a while loop
i = 0  # counts the rounds

while i < 10:  # checked before every round
    print("Keep going")
    i += 1  # without this line, i stays 0 and the loop never ends
else:  # optional: runs once, when the condition comes out False
    print("Done")

# Output:
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Keep going
# Done
