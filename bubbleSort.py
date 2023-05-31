l=[]
l=eval(input("Enter the array"))

s=len(l)
for i in range(0,s):
    for j in range(0,s):
        if l[j] > l[i]:
            t=l[i]
            l[i]=l[j]
            l[j]=t

print(l)