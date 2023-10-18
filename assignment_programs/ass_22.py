# Write a function func1() such that it can accept a variable
# length of argument and print
# all arguments valuefunc1(20, 40, 60) func1(80, 100).


def func1(*arg):
    for x in range(len(arg)):
        print(f'The value of {x} index element is {arg[x]}')


func1(20,40,60)