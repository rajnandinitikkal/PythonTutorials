def Add (x,y):
    return x+y

def Substract (x,y):
    return x-y

def Multiply (x,y):
    return x*y

def Divide (x,y):
    return x/y

print("Hello , Welcome to Rutuja`s simple calculator!!!")
print( " SELECT OPERATION ")
print("1. Add")
print("2. Substract")
print("3. Multiply")
print("4. Divide ")

choice = input("select any one option from the above (1/2/3/4):")

n1 = int(input("Enter your first number: "))
n2 = int(input("Enter your second number: "))



if choice == '1':
    print( n1, "+", n2,  "=", Add(n1,n2) )

elif choice == '2':
    print(n1 , "-" , n2 , "=" , Substract(n1,n2))

elif choice == '3':
    print(n1 ,"*", n2 ,"=",Multiply(n1,n2))

elif choice == '4':
    print(n1, "/",n2,"=",Divide(n1,n2))

else:
    ("Thank you for your efforts!!!")

yes = ("y")
no = ("n")

def recalculation():
    val=(input("Do you want to calculate again (yes/no): "))
    if val == "y":
        print("Hello , Welcome to Rutuja`s simple calculator!!!")
        print( " SELECT OPERATION ")
        print("1. Add")
        print("2. Substract")
        print("3. Multiply")
        print("4. Divide ")

        choice = input("select any one option from the above (1/2/3/4):")

        n1 = int(input("Enter your first number: "))
        n2 = int(input("Enter your second number: "))



        if choice == '1':
            print( n1, "+", n2,  "=", Add(n1,n2) )

        elif choice == '2':
            print(n1 , "-" , n2 , "=" , Substract(n1,n2))

        elif choice == '3':
            print(n1 ,"*", n2 ,"=",Multiply(n1,n2))

        elif choice == '4':
            print(n1, "/",n2,"=",Divide(n1,n2))

        #else:
            #("Thank you for your efforts!!!")
            
        recalculation()

    else:
        print("Thanks for using Rutuja`s calculator")

        
recalculation()