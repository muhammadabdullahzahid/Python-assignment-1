#4. Print the multiplication table of a given number.
number = int(input("Enter a number: "))

print(f"Multiplication table of {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
