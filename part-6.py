# DAY-6
#adjacent characters
#absolute difference
diff=5-7
print(abs(diff)) #absolute
#Ascii values
'''
A-Z(65-)
a-z(97-)
0-9(48-)
'''
macha="D"
print(ord(macha)) #ordinal(for getting asciil values)

# find the score of a string using the ascii and adjacent absolute characters difference
s="abcd"
sum=0
for i in range(len(s)-1):
    a=ord(s[i])
    b=ord(s[i+1])
    temp=abs(a-b)
    sum=sum+temp
print(sum)
    