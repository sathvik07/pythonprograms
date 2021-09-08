nums = [0,1,2,2,3,0,4,2]
val =2
n = len(nums)
if n == None:  
    print("")
while (val in nums):
    nums.remove(val)
print (len(nums))