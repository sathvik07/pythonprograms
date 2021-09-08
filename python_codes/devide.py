def solution():
 dividend = -2147483648
 divisor = -1
#  res = 0
# isNegative = False
# if (devidend < 0):
#     devidend = -devidend
#     isNegative = True 

# while (devidend > devisor):
#    devidend = devidend - devisor
#    res += 1
#    print(devidend)
# print("devison answer is",abs(res))
#  if(dividend > 2147483647):
#             return 2147483647
        
#  if(dividend == -2147483648 and divisor == -1) :
#           return 2147483647


sign = -1 if ((dividend < 0) ^ (divisor < 0)) else 1

if(dividend > 2147483647):
        return 2147483647
        
if(dividend == -2147483648 and divisor == -1) :
        return 2147483647

devisor = abs(divisor)
devidend = abs(dividend)


# if (devidend == 0 or devisor == 0 or devisor ==1):
#     print("cannot devide if it is 0 or 1")
# print(sign)
res = 0
while (devidend >= devisor):
   devidend -= devisor
   res += 1
   print(devidend)

print("devison answer is",sign * res)


