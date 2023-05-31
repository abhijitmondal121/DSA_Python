l=[]
l=eval(input("Enter the array : "))

t=int(input("Enter the number you want to search :"))
f=0
for i in l:
    if i==t:
        f=1
        break

if f==1:
    print("Found")
else:
    print("Not Found")