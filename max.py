def maximum(a,b):

    if a >= b:
        return a
    else:
        return b

a = 33
b = 44
print(maximum(a,b))

# python program to find minimum number

a = 40
b = 23

minimum = min(a,b)
print(minimum)

# python program to find maximum or minimum number

a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))

if a > b:
    print("a is greater than b!")
elif b > a:
    print("b is greater than a!")
elif a==b:
    print("Numbers are equal!!!")
else:
    ("ERROR !!!!!!!!!!!!!")
