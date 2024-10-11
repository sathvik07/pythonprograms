# A = [10,20,30]
# n = len(A)
# maxi = float("-inf")
# for s in range(n):
#     curr_sum = 0
#     for e in range(s,n):
#         curr_sum += A[e]
#         maxi = max(maxi,curr_sum)
#
# print(maxi)


# A = [10,20,30]
# n = len(A)
# sum = 0
# maxi = float("-inf")
# for s in range(n):
#     curr_sum = 0
#     for e in range(s,n):
#         curr_sum += A[e]
#         sum += curr_sum
#
# print(sum)
#
# A = [2,4,8,9,10]
# N = len(A)
# ans = 0
# for i in range(len(A)):
#     # print(i+1)
#     # print("n-i is",N-i)
#     freq = (i+1) * (N-i)
#     contr = freq * A[i]
#     print(contr)
#     ans += contr
#
# print(ans)

N = 10
K = 3
for S in range(0,N-K+1):
    e = K + S - 1
    print(S,e)

