# Given a two list. Create a third list by picking an odd-index element
# from thefirst list  and even index elements from second

list1 = [23,56,8,9,90,60,56,34]
list2 = [45,67,1,4,23,70,68,49]
list3 = []

for x in range(1,len(list1)):
    if x%2 == 1:               #odd indexs
        list3.append(list1[x])


for y in range(len(list2)):
    if y%2 == 0:               #even indexs
        list3.append(list2[y])


print(list3)