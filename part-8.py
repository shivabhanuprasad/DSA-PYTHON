#part-8
#method 1
arr=[6,8,5,10,2]
maxx=arr[0]
for i in range(len(arr)):
    if arr[i]>maxx:
        maxx=arr[i]
print(maxx)
#method 2
arr=[6,8,5,10,2] 
ans=0
for i in range(len(arr)):
    val=arr[i]
    if val>ans:
        ans=val
print(ans)
#method 3
for i in range(len(arr)):
    val=arr[i]
    ans=max(val,ans)
print(ans)

#count the max no of words in the sentence 
s=["hello good how","good bad ugly macha","im proper"]
ans=0
for i in range(len(s)):
    ch=s[i]
    temp=1
    for j in range(len(ch)):
        chj=ch[j]
        if chj==" ":
            temp=temp+1
    ans=max(ans,temp)
print(ans)

'''
TWO SUM PROBLEMM

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
nums=[2,7,11,15]
target=9
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        f1=nums[i]
        f2=nums[j]
        if f1+f2==target:
            print(i,j)
       