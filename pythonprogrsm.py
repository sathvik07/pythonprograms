# a=8
# b=6
# #
# # maxi = lambda a,b: a if a>b else b
# # print(maxi(a,b))
# #
# # x = [a if a>b else b]
# # print(x)
#
# def factorial_recursive(n):
#     # Base case: 1! = 1
#     if n == 1:
#         return 1
#
#     # Recursive case: n! = n * (n-1)!
#     else:
#         print(n)
#         return n * factorial_recursive(n-1)
#
# print(factorial_recursive(5))
def prime(x, y):
    prime_list = []
    for i in range(x, y):
        if i == 0 or i == 1:
            continue
        else:
            print("value of i in else is", i)
            for j in range(2, int(i / 2) + 1):
                print("i value is ",i)
                print("j value is ",j)
                if i % j == 0:
                    print("true")
                    break
            else:
                prime_list.append(i)
    return prime_list


# Driver program
starting_range = 2
ending_range = 7
lst = prime(starting_range, ending_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)