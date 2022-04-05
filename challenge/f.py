n, r, avg = tuple(map(int, input().split()))
a = [0] * n
b = [0] * n

for i in range(n):
    u,v = tuple(map(int, input().split()))
    a[i] = u
    b[i] = v

m = avg * n - sum(a)
if m <= 0:
    print(0)
    exit()

b, a = zip(*sorted(zip(b, a)))

c = 0
for i in range(len(b)):
    if m == 0:
        break
    d = min(m, r-a[i])
    m -= d
    c += d * b[i]
print(c)