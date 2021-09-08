nums1 = [1,2]
nums2 = [3,4]

sum = nums1 + nums2 
sum.sort()
print (sum)

if len(sum)%2==0:
        print((sum[len(sum)//2]+sum[(len(sum)//2)-1])/2)
else:
    print((sum[len(sum)//2]))

#print(sum)