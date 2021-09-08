# height = list(int((input("enter the height"))))

n = int(input("enter the number of elements"))

height = list(map(int,input("enter the numbers : ").strip().split()))[:n]


max_wat = 0
left = 0
right = len(height) -1 

while (left != right):
    max_wat = max(max_wat,(right-left) * min(height[left],height[right]))

    if height [left] < height[right]:
        left += 1
    else:
        right -= 1


print(max_wat)