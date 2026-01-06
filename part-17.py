#TWO FARTHEST HOUSES WITH DIFFERNT COLOURS
colors=[1,8,3,8,7]
n=len(colors)
ans=0
for i in range(n):
    for j in range(i+1,n):
        if colors[i]!=colors[j]:
            temp=j-i
            ans=max(ans,temp)
print(ans)