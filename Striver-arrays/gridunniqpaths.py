def griduniquepaths(i,j,n,m):
    if i == (n-1) and j == (m-1):
        return 1
    if i >= n or j >= m:
        return 0
    else:
        return griduniquepaths(i+1,j,n,m) + griduniquepaths(i, j+1, n, m)


print(griduniquepaths(0,0,2,3))