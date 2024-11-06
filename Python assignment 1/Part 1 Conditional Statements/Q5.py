#5. Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).
grade = float(input("Enter your grade percentage: "))

if grade >= 90:
    print("Your letter grade is: A")
elif grade >= 80:
    print("Your letter grade is: B")
elif grade >= 70:
    print("Your letter grade is: C")
elif grade >= 60:
    print("Your letter grade is: D")
else:
    print("Your letter grade is: F")
             
     