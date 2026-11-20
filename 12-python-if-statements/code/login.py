# the correct username and password
correct_username = "sam_codes"
correct_password = "python123"

# 1. ask for the username and password
username = input("Username: ")
password = input("Password: ")

# 2. both correct: log in
if username == correct_username and password == correct_password:
    print("Login successful!")
    print("Welcome to your homepage.")

# 3. either one wrong: show an error
if username != correct_username or password != correct_password:
    print("Login failed!")
    print("Wrong username or password.")

# Run it again with sam_codes and python123:
# Login successful!
# Welcome to your homepage.

# Output (input: alex | python123):
# Username: alex
# Password: python123
# Login failed!
# Wrong username or password.
