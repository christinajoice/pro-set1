n=int(input("Enter number of values"))
q=int(input("Enter no of queries"))
li=[]
print("Enter values")
for i in range(n):
  a=int(intput())
print("Enter queries")
for i in range(q):
  n=input().split(" ")
  l=int(n[0])
  r=int(n[1])
  while(r):
    l,r=r,l%r
  li.append(l)
for i in range(len(li)):
  print(li[i])
