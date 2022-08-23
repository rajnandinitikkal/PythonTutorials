"""  
def squaresum(n):
    sm = 0
    for i in range(1, n+1):
        sm = sm + (i * i)

    return sm

n = 334
print(squaresum(n))                     

"""

num = int(input("Enter 1st number : "))
num1 = int(input("Enter last number : "))

print("perfect square is as follows : ")

while num<=num1:
    for i in range(1,num1):
        if i*i == num:
            print(num)
                              
    num = num+1 
    