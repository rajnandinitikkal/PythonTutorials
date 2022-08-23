#print("hello Everyone this is Rutuja!")

print("\nHow many elements are there in array?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("\nEnter elelment in Array")
    item = int(input())
    array.append(item)

print("Enter the index from where you want to delete an element")
position = int(input())
array = array[:position] + array[position+1:]
print("Resultant array is\n")
print(array)