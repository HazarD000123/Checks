# Presence Check

email = input("Enter your email address : ")

if email != "":
    print("Nice email!")
else:
    while email == "":
        print("Please re-enter, you cannot leave this empty.")
        email = input("Enter your email address : ")
