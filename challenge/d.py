n = int(input())
a = list(map(int, input().split()))

m = 0
c = []
for i in range(len(a)):
    if a[i] > m:
        c.extend([0] * (a[i] - m))
        m = a[i]

    c[a[i] - 1] += 1

count = 0
if m > len(c):
    c.extend([0] * (m - len(c)))
for i in range(len(c)):
    if c[i] > 1:
        count += 1
        k = c[i] - 1
        for j in range(i + 1, i+k+1):
            c[j] += 1
print(count)