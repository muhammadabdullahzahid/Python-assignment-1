#8. Create a program that checks if a given string is a palindrome.
word = str(input("Enter any word="))
if word == word[::-1]:
    print ("f (word) is a palindrome")
else:
    print ("f (word) is not a palindrome")    