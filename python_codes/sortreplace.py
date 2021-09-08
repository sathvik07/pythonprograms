a = [1,1,2]

n = len(a)
j=0
if n == None:
    print("")
for i in range(n-1):
    if a[i] != a[i+1] :
        a[j] = a[i+1]
        j += 1
print(j+1)



