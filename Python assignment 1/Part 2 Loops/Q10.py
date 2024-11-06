#10. Use a loop to count the number of digits in an integer.
number = int(input("Enter an integer: "))
count = 0

# Use a while loop to count the digits
while number != 0:
    number //= 10  # Remove the last digit from the number
    count += 1

print("The number of digits is:", count)
