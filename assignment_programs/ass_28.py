# Find all occurrences of “USA” in givenstring ignoring the case.

def FindUSA(strr):
    string1= strr.upper()
    lst= string1.split(' ')
    print(lst)
    count=0
    for x in range(len(lst)):
        if lst[x] == "USA":
            count += 1

    print(f'Number of times USA appeared  in  the input \" {strr} \" is {count}')


string2 = str(input("Enter the String to count no. of appearance of \"USA\":"))
FindUSA(string2)