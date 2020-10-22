# contributed by Sakshi Agrawal
from itertools import product
x, m = map(int, input().split())
l = []
p = []
q = []
sum = 0
for i in range(x):
    l.append(list(map(int,input().split())))
    l[i].remove(l[i][0])
p = list(product(*l))
for i in range(len(p)):
    sum = 0
    for j in range(x):
        sum += pow(p[i][j], 2)
    q.append(sum%m)
print(max(q))
