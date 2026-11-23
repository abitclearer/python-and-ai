# the same day planner with match: name the value once, then list the cases
# input gives text, so every case is text too ("1", not 1)
day = input("Enter a day (1-7): ")

match day:
    case "1":
        print("Monday: meeting day")
    case "2":
        print("Tuesday: coding day")
    case "3":
        print("Wednesday: testing day")
    case "4":
        print("Thursday: code review day")
    case "5":
        print("Friday: release day")
    case "6" | "7":  # | means or
        print("Weekend: time to rest")
    case _:  # _ matches anything that's left, like else
        print("Invalid day")

# Other runs:
# 7 -> Weekend: time to rest
# 9 -> Invalid day

# Output (input: 4):
# Enter a day (1-7): 4
# Thursday: code review day
