#part-9
#how to store 2D array
li=[[5,6,7],[1,2,3],[1,2,3]]
#printing each element  
#li[row][col]
print(li[2][2])
#print whole matrix
for i in range(len(li)):
    print(li[i])

# to get better understandhing of matrices we can to identify rows and columns
li=[[5,6,7],[1,2,3],[1,2,3]]
rows=len(li)
col=len(li[0])
print(rows,col)

for i in range(rows):
    for j in range(col):
        print(li[i][j])
        
#print only one row
mat=[[1,2,3,4],[5,6,7,8]]
rows=len(mat)
col=len(mat[0])
for i in range(rows):
    print(mat[i][3])
    

