#Take a user’s age as input and display whether they are a minor, adult, or senior citizen.
age = int(input("Enter your age;"))
if age < 18:
    print ("You are minor.")
elif age >= 18 and age <= 50: 
    print ("Yor are adult.")
else:
    print ("You are Senior.")    