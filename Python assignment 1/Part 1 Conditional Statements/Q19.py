19. #Check if a string input is uppercase, lowercase, or a mix.
text = input ("Enter a string")
if text.isupper():
    print("the string is all uppercase. ")
elif text.islower ():
    print ("the string is all lowercase.")   
else:
    print ("the string is a mix of uppercase and lowercase characters.")     