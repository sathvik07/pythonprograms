nums = [-1,2,1,-4]
target = 1
diff = float('inf')
nums.sort()
for i ,n in enumerate(nums):
    # print(i,n)
    # print("each")
    if i>0 and n == nums[i-1]:
        continue

    
    low , high = i+1 , len(nums)-1

    while low < high:
        sumofthree = n + nums[low] + nums[high]
        if abs(target - sumofthree) < abs(diff):
            diff = target - sumofthree
          
        if sumofthree < target :
            low += 1
        else:
            high -= 1


    if diff == 0 :
        break
print(target - diff)
