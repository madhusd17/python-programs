str=input("Enter a string: ").replace(" ","").lower()
if str==str[::-1]:
    print("it is palindrome")
else:
    print("not a palindrome")
