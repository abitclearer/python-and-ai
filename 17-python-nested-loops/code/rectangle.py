# print a rectangle of stars: width stars across, height rows down
width = int(input("Width: "))    # stars in each row
height = int(input("Height: "))  # number of rows

for row in range(height):      # outer loop: one round per row
    for column in range(width):   # inner loop: one round per star
        print("*", end="  ")   # end="  ": two spaces instead of a new line
    print()                    # row finished: move to a new line

# Output (input: 10 | 5):
# Width: 10
# Height: 5
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
# *  *  *  *  *  *  *  *  *  *
