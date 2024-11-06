# Get the input number from the user
n = int(input("Enter a number: "))

even_sum = 0
odd_sum = 0

# Loop through numbers from 1 to n
for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i  # Add to even_sum if the number is even
    else:
        odd_sum += i   # Add to odd_sum if the number is odd

# Print the results
print(f"The sum of even numbers up to {n} is: {even_sum}")
print(f"The sum of odd numbers up to {n} is: {odd_sum}")
