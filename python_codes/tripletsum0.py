nums = [-1,0,1,2,-1,-4]

length = len(nums)

if length < 2 :
    print("")

result = []
result_set = set()
nums.sort()


for i in range(length):
    if (i>0 and nums[i] == nums[i-1]):
        continue
    j=i+1
    k=length-1
    while j<k:
        triplet_sum = nums[i] + nums[j] + nums[k]
        if triplet_sum == 0 :
            if(nums[i],nums[j],nums[k]) not in result_set :
                result.append([nums[i],nums[j],nums[k]])
                result_set.add((nums[i],nums[j],nums[k]))
            j += 1
            k -= 1
        elif triplet_sum < 0:
            j += 1
        else:
            k -= 1
print (result)

