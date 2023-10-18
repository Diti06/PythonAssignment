# . Accept list of 5 float numbers as a inputfrom user.
lst=[]
no_ele= int(input("Enter the no of elements you want in list:"))

for x in range(no_ele):
    num = float(input(f'Enter the element {x+1}  of the list:'))
    lst.append(num)

print(f'The list is : {lst} ')