# python program to swap first
# and last element of a list 

# swap function
def swapList(newList):
    size = len(newList)

    # swapping 
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1] = temp

    return newList

# driver code
newList = [12, 35,9,56,24]

print(swapList(newList))