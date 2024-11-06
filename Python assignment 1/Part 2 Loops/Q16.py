#16. Create a program to calculate the sum of the digits of an inputted integer.
# Get the input number from the user
number = int(input("Enter an integer: "))
digit_sum = 0

# Loop through each digit of the number
while number != 0:
    digit_sum += number % 10  # Add the last digit to the sum
    number //= 10  # Remove the last digit

# Print the result
print("The sum of the digits is:", digit_sum)
