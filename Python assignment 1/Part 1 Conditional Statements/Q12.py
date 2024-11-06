#12. Write a program that takes a temperature in Celsius and checks if it’s freezing, moderate, or hot.
temperature = int (input ("enter the temperture in celsius="))
if temperature <= 0:
    print ("the temperature is freezing")
elif temperature >= 0 and temperature <= 22:
    print ("the temperature is moderate")  
else:
    print ("the temperature is hot")    
