
nums = [1,0,-1,0,-2,2]
target = 0
ans =[]
n =len(nums)
nums.sort()
i= 0
for i in range(n-3):
            for j in range(i+1,n-2):
                k = j+1
                l = n-1
                while(k<l):
                    x = nums[i]+nums[j]+nums[k]+nums[l]
                    if(x==target):
                        ans.append([nums[i],nums[j],nums[k],nums[l]])
                        k+=1
                        l-=1
                    elif x<target:
                        k+=1
                    else:
                        l-=1
final =[]
for i in ans:
        if i not in final:
                final.append(i)
print(final)