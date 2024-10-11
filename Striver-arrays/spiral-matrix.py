def spiral_matrix(a):

    ans = []

    n = len(a)
    m = len(a[0])

    top = 0
    left = 0
    right = m-1
    bottom = n-1

    while top <= bottom and left <= right:
        for i in range(left,right+1):
            ans.append(a[top][i])
        top += 1

        for i in range(top, right+1):
            ans.append(a[i][right])
        right -= 1
        print(ans)


        if top <= bottom:
            for i in range(right, left-1, -1):
                ans.append(a[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top-1, -1):
                ans.append(a[i][left])
            left += 1

    return ans


a = [[1, 2, 3, 4],
       [5, 6, 7, 8],
       [9, 10, 11, 12],
       [13, 14, 15, 16]]


print(spiral_matrix(a))