age=int(input("Enter your age :"))
BMI=float(input("Enter your BMI :"))

if age<60 and BMI<30:
    print("Low risk")
elif age>60 and BMI<30:
    print("Medium risk")
elif age<60 and BMI>30:
    print("Medium risk")
elif age>=60 and BMI>=30:
    print("High risk")
else:
    print("ERROR")