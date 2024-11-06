#13. Use nested loops to print a pyramid pattern of *.
rows = 5  # Number of rows in the pyramid

for i in range(1, rows + 1):
    # Print leading spaces
    for j in range(rows - i):
        print(" ", end="")
    
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    
    # Move to the next line after each row
    print()
