# # Given a two list of numbers create a new list such that new list should contain only odd
# # numbers from the firstlist and even numbers from the secondlist
# def OddList(a):
#     final_list=[]
#     for x in range(len(a)):
#         if a[x]%2==0:
#             pass
#         else :
#             final_list.append(a[x])
#     return final_list
#
# list1=[23,40,50,79,20]
# list2=[34,67,87,89,90]
#
# new_list1= OddList(list1)
# new_list2= OddList(list2)
# mfinal_list= new_list1 + new_list2
# print(mfinal_list)
#
#
#
#
#
#
# 9. Given a two list of numbers create a new list such that new list should contain only odd
# numbers from the firstlist and even numbers from the secondlist.

print("Enter how many numbers you want to add to two different lists:")
n1 = int(input("Enter the number of elements for the first list: "))
n2 = int(input("Enter the number of elements for the second list: "))

list1 = []
list2 = []
list3 = []

print("Enter values for the first list:")
for i in range(n1):
    val1 = int(input(f"Enter value {i+1} for list1: "))
    list1.append(val1)

print("Enter values for the second list:")
for j in range(n2):
    val2 = int(input(f"Enter value {j+1} for list2: "))
    list2.append(val2)

for x in range(n1):
    if list1[x] % 2 == 0:
        list3.append(list1[x])

for y in range(n2):
    if list2[y] % 2 == 0:
        pass
    else:
        list3.append(list2[y])

print("Resulting list containing even numbers from the first list and second list:", list3)
