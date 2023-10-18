
# Write a function calculation () such that it can accept two variables and calculate the
# addition and subtraction of it. And also it must return both addition and subtraction in a
# single return call.

def calculation(a,b):
    d= a+b
    e= a-b
    return d,e


input1= int(input("Enter 1st no"))
input2= int(input("Enter 2nd no"))

answer_add,answer_sub= calculation(input1,input2)
print('The answer of addition is: ',answer_add,'The answer of subtraction: ', answer_sub)
