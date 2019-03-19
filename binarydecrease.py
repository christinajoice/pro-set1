#christinajoice

n=int(input("Size of array"))
a=input().split()
b=[]
c=[]
for i in range(n):
  b.append(bin(int(a[i]))[2:])
  c.append(b[i].count('1'))
for i in range(0,n-1):
  for j in range(1,n):
    if i!=j:
      if c[i]<c[j]:
        a[i],a[j]=a[j],a[i]
      elif c[i]==c[j]:
        if a[i]<a[j]:
          a[i],a[j]=a[j],a[i]
print(a)  
