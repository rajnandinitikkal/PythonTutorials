# A number based on python program to find sum 
# of series with cubes of first n natural
# numbers

# Return the sum of series
"""
def sumOfSeries(n):
    x = (n*(n+1)/2)
    return (int(x*x))

n = 5
print(sumOfSeries(n))

"""



   
# Efficient python program to find sum of cubes 
# of first n natural numbers that avoids
# overflow if result is going to be withing
# limits.

# Returns the sum of series
def sumOfSeries(n):
    x = 0
    if n % 2 == 0:
        x = (n/2) * (n+1)
    else:
        x = ((n+1)/2)*n

    return (int)(x * x)

n = 23
print(sumOfSeries(n))






