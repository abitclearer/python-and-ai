# a string is a collection of characters: the for loop takes them one at a time
msg = input("Enter some text: ")

for ch in msg:  # each round, ch holds the next character
    print(f"Item: {ch}")
else:  # optional: runs once, after the last character
    print("Loop finished")

# Output (input: Hi, Python!):
# Enter some text: Hi, Python!
# Item: H
# Item: i
# Item: ,
# Item:  
# Item: P
# Item: y
# Item: t
# Item: h
# Item: o
# Item: n
# Item: !
# Loop finished
