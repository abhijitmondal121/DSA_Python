l=[]
l=eval(input("Enter the array.."))

s=len(l)

for i in range(1,s):
    j=i-1
    key=l[i]
    while j>=0 and key<l[j]:
        l[j+1]=l[j]
        j-=1
        
    l[j+1]=key
    
print(l)