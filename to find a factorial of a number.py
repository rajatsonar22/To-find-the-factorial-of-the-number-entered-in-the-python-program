#program to find a factorial of a number
import math
print("---Finding the factorial of a numbers")
n1 = int(input("Enter a number "))
print("Factorial is",math.factorial(n1))

#Finding factorial using recursive function
print("---Finding factorial using recursive function")
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = int(input("Enter a number"))
print("The factorial of",num ,"is",factorial(num))
        
