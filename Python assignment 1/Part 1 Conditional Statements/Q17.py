#17. Write a program that asks for an integer and checks if it’s divisible by 2, 3, or both.
number = int (input ("Enter an integer"))
if number %2 == 0:
    print ("number is divisible by 2")
elif number %3 == 0:
    print ("number is divisible by 3") 
else:
    print ("number is not divisible by 2 and 3")       