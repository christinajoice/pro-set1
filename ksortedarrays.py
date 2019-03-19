k=int(input("no of arrays"))
a=[]
b=[]
for i in range(k):
  a.append(input().split())
for i in range(k-1):
  b=a[i]+a[i+1]
b.sort()
print(' '.join(b))
