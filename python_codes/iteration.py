import timeit;

mysetup = "import timeit"


myocde ='''def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while (n > 1):
            fact *= n
            n -= 1
        return fact'''


"""num = 5;
print("Factorial of", num, "is",factorial(num))"""

print timeit.timeit(setup=mysetup,stmt=myocde,number=10000)