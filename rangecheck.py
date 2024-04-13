# Range Check

student_mark = int(input("Enter the student marks : "))

while True:
    if student_mark < 0 or student_mark > 100:
        print("Re-enter the marks, it should be within the range 0 and 100.")
        student_mark = int(input("Enter the student marks : "))
    else:
        print("It is within the range.")
        break
