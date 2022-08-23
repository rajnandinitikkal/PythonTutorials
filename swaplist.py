# python3 program to swap first 
# and last element of a list

# swap function
def swapList(newList):

    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

# driver code 
newList = [12,35,9,56,24]
print(swapList(newList))


# python program to illustrate
# the usage of * operand

list = [1, 2, 3, 4]


a, *b, c = list

print(a)
print(b)
print(c)


# python3 program to swap first
# and last element of a list

# swap function
def swapList(list):

    start, *middle, end = list
    list = [end, *middle, start]

    return list
newList = [12, 35, 9, 56, 24]

print(swapList(newList))

# python3 program to swap first
# last element of a list 

# swap function 
def swapList(list):

    first = list.pop(0)
    last = list.pop(-1)

    return list

newList = [12, 35, 9, 56, 24]

print(swapList(newList))