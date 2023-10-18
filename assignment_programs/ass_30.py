# Given a list iterate it and count the occurrence of each element and
# create a dictionary to show the count of each element

list1 = [1,34,5,6,78,90,34,5,6]

unique_list =[]
y=0
for x in list1:
    if  x not in unique_list:
        unique_list.append(list1[y])
        y = y+1
print(unique_list)
