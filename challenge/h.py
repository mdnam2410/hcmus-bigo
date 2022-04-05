import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

n, d = tuple(map(int, input().split()))
x = list(map(int, input().split()))

m = max(x)
t = [0] * (m+1)
b = [0] * (m+1)
for i in range(len(x)):
    b[x[i]] = 1
    for j in range(min(0, x[i] - d + 1), min(x[i], m) + 1):
        t[j] += 1

g = lambda x: ncr(x, 3) if x >= 3 else 0
count = 0
for i in range(m):
    if b[i] == 1 and t[i] >= 3:
        count += g(t[i])
print(count, t, b)