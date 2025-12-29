# max diff from num[i]<num[j]
'''
(i.e., nums[j] - nums[i]), such that 0 <= i < j < n and nums[i] < nums[j].
'''
nums=[7,1,5,4]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i+1,n):
        if nums[i]<nums[j]:
            temp=nums[j]-nums[i]
            ans=max(temp,ans)
print(ans)