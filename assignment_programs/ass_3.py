# Given a string, display only those characters which are present at an evenindex number.

def StringTrimmer(a):
    lst = list(a)

    for x in range(len(lst)):
        if(x%2==0):
         print(lst[x])

sttr = str(input("Enter the String:"))

StringTrimmer(sttr)