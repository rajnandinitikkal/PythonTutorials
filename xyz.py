# function fornth fibonacci number

def fibonacci(n):
    if n<= 0:
        print("Incorrect Input")
        # first fibonacci number is 0
    elif n == 1:
        return 0
    # second fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(10))