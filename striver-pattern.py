# 1
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end="")
#     print()

# 2
n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()


# 3
# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end="")
#     print()


# 4
# for i in range(n):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()


# 5
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()


# 6
# for i in range(n,0,-1):
#     for j in range(i):
#         print(j+1,end="")
#     print()

# 7
# for i in range(1,n+1):
#     print(" " * (n-i+1) + "*" * ( 2 * i -1) + " " * (n-i+1))

# 8
# for i in range(n, 0, -1):
#     print(" " * (n-i+1) + "*" * ( 2 * i -1) + " " * (n-i+1))


# 9
# for i in range(1,n+1):
#     print(" " * (n - i + 1) + "*" * (2 * i - 1) + " " * (n - i + 1))
# for i in range(n,0,-1):
#     print(" " * (n - i + 1) + "*" * (2 * i - 1) + " " * (n - i + 1))

# 10
# for i in range(n):
#     for j in range(i+1):
#         print("*", end="")
#     print()
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*", end="")
#     print()

# 11
# for i in range(1,n+1):
#     if i % 2 == 0:
#         for j in range(i):
#             if j % 2 != 0:
#                 print("1", end="")
#             else:
#                 print("0", end="")
#     else:
#         for j in range(i):
#             if j % 2 == 0:
#                 print("1", end="")
#             else:
#                 print("0", end="")
#     print()


# 12
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     for j in range(0,2*n-2*i):
#         print(" ", end="")
#     for j in range(i, 0, -1):
#         print(j,end="")
#     print()


# 13
# count = 0
# for i in range(n):
#     for j in range(i+1):
#         count += 1
#         print(count,end=" ")
#     print()


# 14
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+j), end="")
#     print()

# 15
# for i in range(n,0,-1):
#     for j in range(i):
#         print(chr(65+j), end="")
#     print()


# 16
# for i in range(n):
#     for j in range(i+1):
#         print(chr(65+i), end="")
#     print()


# 17
# for i in range(1,n+1):
#     for j in range(1,n+1-i):
#         print(" ", end="")
#     for j in range(1,i+1):
#         print(chr(64+j), end="")
#     for j in range(i-1, 0, -1):
#         print(chr(64+j), end="")
#     print()


# 18
# for i in range(n,0,-1):
#     for j in range(i, n+1,1):
#         print(chr(65+(j-1)), end="")
#     print()


# 19
# for i in range(1,n+1):
#     print("*" * (n - i + 1) + " " * (2 * i - 1) + "*" * (n - i + 1))
# for i in range(n,0,-1):
#     print("*" * (n - i + 1) + " " * (2 * i - 1) + "*" * (n - i + 1))


# 20
# for i in range(1,n+1):
#     print("*" * i, end="")
#     print(" " * (n-i) * 2, end="")
#     print("*"*i)
# for j in range(n,0,-1):
#     print("*" * j, end="")
#     print(" "* (n-j) * 2, end="")
#     print("*" * j)


# 21
# for i in range(1,n):
#     for j in range(1,n):
#         if i == 1 or j == 1 or i == n-1 or j == n-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()

for i in range(2*n-1):
        for j in range(2*n-1):
            top = i
            bottom = j
            right = (2*n - 2) - j
            left = (2*n - 2) - i
            print(n-min(min(top,bottom), min(left,right)),end=" ")
        print()
