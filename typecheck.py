# Type Check

brothers = float(input("How many brothers do you have : "))

if brothers == (brothers//1):
        print("Nice family!")
else:
        while brothers != (brothers//1):
            print("This must be a whole number, please re-enter.")
            brothers = int(input("How many brothers do you have : "))
