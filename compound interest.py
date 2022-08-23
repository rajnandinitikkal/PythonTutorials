# python program to find compound interest for given values

def compound_interest(principle,rate,time):

    # calculate compound interest
    Amount = principle * (pow ((1 + rate / 100),time))
    CI = Amount - principle
    print("Compound interest is",CI)

compound_interest(10000, 10.25 , 5)

# This code is contributed ny Abhishek Agrawal.