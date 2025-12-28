#undeerstanding the time and space complexity
#with the help of one problem 
'''
O(1)- one search time
O(n)- n times
O(log(n))- half of the time
O(n^2)- double time

O(n^2)> O(log(n))> O(n)> O(1)
'''
prices = [7,1,5,3,6,4]
minval=prices[0]
ans=0
for i in range(1,len(prices)):
    ans=max(ans,prices[i]-minval)
    minval=min(minval,prices[i])
print(ans)
"""
when time exceeds we need to solve in optimal wayss
"""