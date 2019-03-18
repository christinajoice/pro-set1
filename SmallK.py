#christinajoice

a=input("Enter a number")
k=int(input("Enter k value"))
l=len(a)
li=[]
sublen=l-k
for i in range(0,k+1):
  li.append(a[i:sublen])
  sublen=sublen+1
print(min(li))
  
