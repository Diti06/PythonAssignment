# Given a string of odd length greater 7, return a string
# made of the middle threechars of a given String

stri= str(input("Enter the string of length 7"))
lst= stri.split()
if len(lst) != 7:
    print("invalid length. Enter valid string")

new_list= lst[2]+lst[3]+lst[4]

final_str= str(new_list)
print("The middle three characters of the given string is:", final_str)
