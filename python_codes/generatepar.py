n= int(input("enter the number"))
brackets = ["()"]
lit = []
i=1
for i in range (n+1):
     if i <= 0:
         print("")
     else:
      lit.append(i*"(" + i*")")


print(lit)
