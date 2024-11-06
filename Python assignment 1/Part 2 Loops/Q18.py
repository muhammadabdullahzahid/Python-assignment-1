# 18. Use a loop to print numbers in reverse order within a given range.

# Get the start and end values for the range from the user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Loop to print numbers in reverse order
for number in range(end, start - 1, -1):
    print(number)
