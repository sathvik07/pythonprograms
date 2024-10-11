def leaderscount(a,n):
    ans = []
    max_v = a[n-1]
    ans.append(a[n-1])
    for i in range(n-2, -1, -1):
        if a[i] > max_v:
            ans.append(a[i])
            max_v = a[i]
    return ans

a = [10, 22, 12, 3, 0, 6]
print(leaderscount(a,len(a)))


