# Reverse a given number and return true
# if it is the same as the original number.

a= int(input("Enter a number"))
secret_no= 79
if a == secret_no:
    stri = str(secret_no)
    # reversed_str= stri[::-1]
    reversed_str= stri[::-1]
    reversed_no = int(reversed_str)
    print('True')
    print("The Reversed NUmber is :",reversed_no)

else:
    print('False')

