# three valid accounts (practice only: real apps never keep passwords in the code)
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "admin123":
    print("Login successful (account 1)")
elif username == "root" and password == "root2026":
    print("Login successful (account 2)")
elif username == "sam_codes" and password == "python123":
    print("Login successful (account 3)")
else:
    print("Login failed: wrong username or password")

# Run it again with aa and 111:
# Login failed: wrong username or password

# Output (input: sam_codes | python123):
# Username: sam_codes
# Password: python123
# Login successful (account 3)
