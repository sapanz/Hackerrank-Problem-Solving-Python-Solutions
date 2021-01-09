a=list(map(int,input().split()))
b=list(map(int,input().split()))
bob=0
alice=0
for i in range(3):
 if a[i]>b[i]:
  alice=alice+1
 elif a[i]<b[i]:
  bob=bob+1

print(alice,end=' ')
print(bob)

