# Given a list of numbers, Iterate it and print only those numbers
# which are divisible of 5.

def MultipleOfFive(user_list):
    lst = []
    for x in range(len(user_list)):

        if user_list[x] % 5 == 0:
            lst.append(user_list[x])

    print(f'The numbers that are divisible by 5 in the given list is: {lst}')


l = [30,40,38,68]
print(l)
MultipleOfFive(l)
