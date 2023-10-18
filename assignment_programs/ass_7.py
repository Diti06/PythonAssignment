# Return the total count of string “Emma” appears in
# the given string

def FindEmma(strr):
    lst= strr.split(' ')
    print(lst)
    count=0
    for x in range(len(lst)):
        if lst[x] == "Emma":
            count += 1

    print(f'Number of times Emma appeared  in  the input \" {strr} \" is {count}')

stri= str(input("Enter the String to count no. of appearance of \"Emma\":"))
FindEmma(stri)
