def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1) # in this line when the return is passsed it goes into factorial(n-1) and sits there and reitrtals through all of the numbers


print(factorial(3))