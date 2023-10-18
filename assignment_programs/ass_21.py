# Given a list iterate it and display numbers which are divisible
# by 5 and if you find number  greater than 150 stop the loop iteration.
# list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200].

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
list2=[]
for x in range(len(list1)):
    if list1[x] <= 150 and list1[x] % 5 == 0:
        list2.append(list1[x])

    elif list1[x] > 150:
        break
print(list2)



