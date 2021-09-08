x=-123
rev = 0 
isNegative = False
if (x < 0):
    x = -x
    isNegative = True 


while(x>0):
    remainder = x%10
    x=x//10
    rev= rev * 10 + remainder
print(rev)

if not (rev >= -2147483648 and rev <= 2147483647):
    print(rev)


# if rev in range(-2147483648 ,2147483647):