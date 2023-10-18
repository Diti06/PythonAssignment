# Given 2 strings, s1 and s2, create a newstring by appending s2 in the middle ofs1.


def append_in_middle(s1, s2):
    list1= s1.split()
    list2= s2.split()

    middle_index = len(list1) // 2
    new_list = list1[:middle_index] + list2 + list1[middle_index:]
    new_string = " ".join(new_list)
    return new_string


s1 = str(input("Enter String1 : "))
s2 = str(input("Enter String2 : "))
result = append_in_middle(s1, s2)
print(result)