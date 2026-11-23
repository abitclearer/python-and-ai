# one case can match several values: lowercase w, capital W, or the word up
command = input("Command: ")

match command:
    case "w" | "W" | "up":
        print("Moving up")
    case "s" | "S" | "down":
        print("Moving down")
    case _:
        print("Unknown command")

# Output (input: W):
# Command: W
# Moving up
