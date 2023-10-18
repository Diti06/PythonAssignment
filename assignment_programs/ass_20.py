# Print the following pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

for x in range(1,6):
    for y in range(1,x+1):
        if y > x:
            break
        else:
            print(y, end=" ")
    print()