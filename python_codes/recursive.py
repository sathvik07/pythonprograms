import timeit;

mysetup = "import timeit"

mycode = '''def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1);'''

"""num = 5;
print("Factorial of", num, "is",factorial(num))"""





print timeit.timeit(setup = mysetup,
                    stmt = mycode,
                    number = 10000)