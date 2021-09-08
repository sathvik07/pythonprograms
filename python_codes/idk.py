n=int(input("Enter number of test cases:"))
for i in range(n):
    D,d,p,q=map(int,(input()).split())
    print (D)
    print (d)
    print (p)
    print (q)
    total=0
    step=0
    for j in range(0,D-d,d):
        n=p+step*q
        n=n*d
        total+=n
        step+=1

    n=p+step*q
    n=n*(D%d) if D%d>0 else n*d
    total+=n
    
    print(total)