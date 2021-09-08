nums = [1,0,-1,0,-2,2]
# nums = [2,2,2,2]
target = 0


length = len(nums)

# if length < 4 :
#     print("")

result = []
result_set = []

nums.sort()

# nums = [1,0,-1,0,-2,2]
i=0
for i in range(length-3):
    for j in range (i+1,length-2):
    # if i>0 and nums[i] == nums[i-1]:
    #     continue
    # j=i+1
       k=length - 1
       l = j + 1
       while l<k :
          quad_sum = nums[i] + nums[j] + nums[k] + nums[l]
          if quad_sum == target :
            if([nums[i] , nums[j] , nums[k] , nums[l]]) not in result_set:
                result.append([nums[i] , nums[j] , nums[k] , nums[l]])
                result_set.append(([nums[i] , nums[j] , nums[k] , nums[l]]))

                l += 1
                k -= 1
          elif quad_sum < target :
              l += 1
            #   l += 1
          else :
              k -= 1

# for i in result:
#     if i not in result_set:
#         result_set.append(i)

print(result)                