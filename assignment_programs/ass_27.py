# Given 2 strings, s1, and s2 return a newstring made of the first,
# middle and lastchar each input string

def first_middle_end(s):
    middle_index = len(s)//2
    list1= s[0]+s[middle_index]+s[-1]
    f_string= "".join(list1)
    return f_string


s1= str(input("Enter String1: "))
s2= str(input("Enter String2: "))

final_list= first_middle_end(s1)+ first_middle_end(s2)
final_string= "".join(final_list)
print(final_string)