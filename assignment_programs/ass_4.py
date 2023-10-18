# Given a string and an integer number n,remove characters from a string starting from
# zero up to n and return a new string
#  xs = ['1', '2', '3']
# s = ''.join(xs)


def StringPopper(stringg,num):
    # l= stringg.split()
    lst = list(stringg)
    for x in range(num+1):
       new_lst= list(lst.pop(x))

    print(new_lst)

st= str(input("Enter the string:"))
n= int(input("Enter the value of integer:"))

StringPopper(st,n)


