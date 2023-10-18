# Given a range of first 10 numbers, Iterate from start number to the end number and
# print the sum of the current number and previous number

print('The sum of current number and the previous number is as follow:')
for x in range(1,11):
    sum = x + (x-1)
    print(f'The sum of {x} and {x-1} is {sum}')



