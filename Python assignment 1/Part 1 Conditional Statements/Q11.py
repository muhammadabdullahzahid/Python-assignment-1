#11. Check if a given number is a multiple of both 3 and 5.
# Get a number from the user
number = int(input("Enter a number: "))

# Check if the number is a multiple of both 3 and 5
if number % 3 == 0 and number % 5 == 0:
    print(number, "is a multiple of both 3 and 5.")
else:
    print(number, "is not a multiple of both 3 and 5.")
