def getmissingNo(A):
    n =len(A)
    total = (n+1)*(n+2)/2
    sum_of_A = sum(A)
    return total - sum_of_A

A = [1,2,4,5,6]
miss = getmissingNo(A)
print(miss)
