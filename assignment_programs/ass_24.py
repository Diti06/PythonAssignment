# Write a recursive function to calculate the sum of numbers from 0 to 10.


def recursiveadd(num):

    if num == 0 :
        return 1

    else:
        return num+recursiveadd(num-1)


sum1 = recursiveadd(10)

print('The sum is', sum1)


