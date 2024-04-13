# Length Check

pwd = input("Enter your password : ")

if len(pwd) == 8:
        print("Correct")
else:
            while len(pwd)!= 8:
                print("Your password must be exactly 8 letters, please re-enter.")
                pwd = input("Enter your password : ")
