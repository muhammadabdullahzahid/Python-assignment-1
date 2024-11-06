#15. Write a program to check if a number is within a specified range.
start = int (input("enter start num="))
end = int (input ("enter end num="))
num = int (input ("enter any number"))
if  start <= num <= end:
    print ("(num) is in specified range")
else:
    print ("(num) is not in specified range")    
