# Functions

# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.


a=float(input("Enter Score : "))

if  a >= 0.9 and a <= 1.0:
    print("A grade")
elif a >= 0.8 and a < 0.9:
    print("B grade")
elif a >= 0.7 and a < 0.8:
    print("C grade")
elif a >= 0.6 and a < 0.7:
    print("D grade")
elif a < 0.6 and a >= 0.0:
    print("F grade")
else:
    print("Wrong Score Entered !")