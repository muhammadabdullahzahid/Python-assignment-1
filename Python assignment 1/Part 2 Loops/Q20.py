# 20. Create a program that simulates a countdown timer starting from a given number down to zero.
# Get the starting number for the countdown
start = int(input("Enter the number to start the countdown: "))

# Countdown loop
for number in range(start, -1, -1):
    print(number)
