numbe = input("enter the number")

num = numbe.strip()

if num[0] == '+' :
    sig = '+'
 
elif num[0] == '-':
     sig = '-'
    
else:
    sig = '+'

# isNegative = False
# if (x < 0):
#     x = -x
#     isNegative = True 

numr = int(num)

if numr in range(-2147483648 ,2147483647):
    print(numr)