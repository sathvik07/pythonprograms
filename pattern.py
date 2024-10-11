# N = 5
#
# for i in range(1,N):
#     for j in range(i):
#         print(i,end=" ")
#     print()

# N = 5
# for i in range(1,N):
#     for j in range(i):
#         print("* ",end = " ")
#     print()
#
# for i in range(N,0,-1):
#     for j in range(i):
#         print("* ",end = " ")
#     print()

# N = 5
# for i in range(1,N):
#     print(i * "* ")

# N = 5
# for i in range(N):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# k = 1
# for i in range(5):
#     for j in range(k):
#         print("*",end=" ")
#     k = k + 2
#     print()

# n = 5
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end=" ")
#
#     print()

# A = [1,2,3]
# A = [3,4,2]
# # A = [2]
# n = len(A)
# pv = 0
# ans = 0
# i = 0
#
# if n == 1:
#     ans = A[0]
#     pv = 1
#
# while i < n-1:
#     if i == 0:
#         if A[i] > A[i+1]:
#             ans = A[i]
#             pv = 1
#     else:
#         print(i)
#         if A[i-1] < A[i] > A[i+1]:
#             ans = A[i]
#             pv = 1
#         elif A[i-1] < A[i] < A[i+1]:
#             print("hii")
#             ans = A[i+1]
#             pv = 1
#     i += 1
#
# if pv == 1:
#     print(ans)
#     print("yes")
# else:
#     print("No")


# A.sort()
# print(max(A))





# def findpeak(A,st,en,n):
#     if n == 1:
#         return 0
#
#     while st < en:
#         mid = st + (en-st) // 2
#         if A[mid+1] > A[mid]:
#             st = mid + 1
#         else:
#             en = mid
#
#     return st
#
#
# A = [1,2,3]
# n = len(A)
# st = 0
# en = n - 1
#
# print(findpeak(A,st,en,n))



# print(3//2)


# def getMinMax(a, n):
#     mini = a[0]
#     maxi = 0
#     for i in range(n):
#         if a[i] > maxi:
#             maxi = a[i]
#         elif a[i] < mini:
#             mini = a[i]
#
#     return mini, maxi
#
#
# a = [3, 2, 1, 56, 10000, 167]
# n = len(a)
# print(getMinMax(a,n))

#
# def subArraySum(arr, n, s):
#     # Write your code here
#     if n == 1:
#         if s == arr[0]:
#             return 1, 1
#         else:
#             return -1
#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             summ += arr[j]
#             if summ == s:
#                 return i + 1, j + 1
#
#     return -1
#
#     # return -1
#     # return -1
#
#
# # arr = [1,2,3,7,5]
# arr = [0]
# n = len(arr)
# # print(n)
# s = 1
# print(subArraySum(arr, n, s))



# def findaverageofsubarrays(A,k):
#     ans = []
#     s = 0
#     WSum = 0
#     # print(len(A))
#     for we in range(len(A)):
#         print(we)
#         WSum += A[we]
#
#         if we >= k-1:
#             ans.append(WSum/k)
#
#             WSum -= A[s]
#
#             s += 1
#
#     return ans
#
# print(findaverageofsubarrays([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))


def findsmallestsubarrayofgivensum(A,s):
    WSum = 0
    Minlen = float("inf")
    Ws = 0

    for We in range(len(A)):

        WSum += A[We]

        while WSum >= s:
            Minlen = min(Minlen, We-Ws+1)

            WSum -= A[Ws]
            Ws += 1


    if Minlen == "inf":
        return 0

    return Minlen


print(findsmallestsubarrayofgivensum([2, 1, 5, 2, 3, 2], 7))
print(findsmallestsubarrayofgivensum([2, 1, 5, 2, 8], 7))
print(findsmallestsubarrayofgivensum([3, 4, 1, 1, 6], 8))