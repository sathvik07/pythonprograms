# def subArraySum(arr, n, s):
#     # Write your code here
#     # if n == 1:
#     #     if s == arr[0]:
#     #         return 1, 1
#     #     else:
#     #         return -1
#
#     for i in range(n):
#         summ = 0
#         for j in range(i, n):
#             summ += arr[j]
#             if summ == s:
#                 return i + 1, j + 1
#
#     return -1
#
# arr = [0]
# n = len(arr)
# s = 1
# print(subArraySum(arr, n, s))


# def segregateElements(arr, n):
#     # Your code goes here
#     print(n)
#     if arr[0] < 0:
#         ele = arr.pop()
#         arr.append(ele)
#
#     i = 1
#     while i < n:
#         if arr[i] < 0:
#             ele = arr.pop(i)
#             arr.append(ele)
#             i -= 1
#         else:
#             i += 1
#
#     return arr


def segregateElements(arr, n):
    # Your code goes here
    pos = []
    neg = []
    for i in range(n):
        if arr[i] < 0:
            neg.append(arr[i])
        else:
            pos.append(arr[i])

    return pos+ neg


arr = [1, -1, 3, 2, -7, -5, 11, 6]
n = len(arr)
print(n)
print(segregateElements(arr,n))
