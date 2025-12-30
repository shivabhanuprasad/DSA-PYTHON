# part -16

nums=[7,1,5,4]
n=len(nums)
ans=0
for i in range(n):
    for j in range(i+1,n):
        if nums[j]>nums[i]:
            temp=nums[j]-nums[i]
            ans=max(ans,temp)
print(ans)

#optimization 
nums=[7,1,5,4]
n=len(nums)
ans=-1
low=nums[0]
for j in range(1,n):
    if low<nums[j]:
        temp=nums[j]-low
        ans=max(ans,temp)
    low=min(low,nums[j])
print(ans)

#
li=[4,5,7,8]
print(li)
#without need square braces
print(*li)

#append
n=5
li=[]
#li=[i for in range(n)] /list comprehension or single list creation
for i in range(n):
    li.append("Shiva")
    
print(li)
  
#optimizing lines in python
print(*[i*2 for i in range(5)])
#you can use this for strings also
print(*[str(i*2)+"sh" for i in range(5)])

#reverse of string
li="shiva"
print(li[::-1])
    
    