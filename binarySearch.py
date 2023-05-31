l=[]
l=eval(input("Enter the array : "))

t=int(input("Enter the value you want to search:"))

s=0
e=len(l)-1
f=0

while(s<e):
    mid=s+(e-s)//2 
    
    if(l[mid]==t):
        f=1
    
    if l[mid] < t:
        s=mid+1
    else:
        e=mid-1
        

if f==1:
    print("Found")
else:
    print("Not found")