# the day planner written with if and elif: every condition repeats day ==
day = input("Enter a day (1-7): ")

if day == "1":
    print("Monday: meeting day")
elif day == "2":
    print("Tuesday: coding day")
elif day == "3":
    print("Wednesday: testing day")
elif day == "4":
    print("Thursday: code review day")
elif day == "5":
    print("Friday: release day")
elif day == "6" or day == "7":
    print("Weekend: time to rest")
else:
    print("Invalid day")

# Output (input: 4):
# Enter a day (1-7): 4
# Thursday: code review day
