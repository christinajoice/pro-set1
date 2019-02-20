n=int(input("Enter a number of strings"))
m=int(input("Enter the length of strings"))
print("Enter the strings")
str=[]
for i in range(0,n):
  str.append(input())
pre=list(set(str[0])&set(str[1]))
for i in range(2,n):
  pre=list(set(pre)&set(str[i]))
print(''.join(pre))
