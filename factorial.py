# python program to find factorial of given number

def factorial(n):

    # single line to find factorial
    return 1 if ( n==1 or n==0) else n * factorial(n-1);

#Driver code
num = int(input("Enter number : "));
print("factorial of" , num,"is",factorial(num))

############************************************###################

def factorial(n):
    return 1 if(n==1 or n==0) else n*factorial(n-1);

num = int(input("Enter a number : "));
print("Factorial of",num,"is",factorial(num))


    
