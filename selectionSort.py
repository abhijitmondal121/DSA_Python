l=[]
l=eval(input("Enter the array"))

s=len(l)


for i in range(s):
    min_idx = i
    for j in range(i+1, s):
        if l[j] < l[min_idx]:
            min_idx = j
    
    t=l[i]
    l[i]=l[min_idx]
    l[min_idx]=t

print(l)