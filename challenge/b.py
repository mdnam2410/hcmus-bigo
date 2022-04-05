N = int(input())
L = list(map(int, input().split()))

d = dict()
max = 0
count = 0
for i in range(len(L)):
    if L[i] not in d:
        d[L[i]] = 0
        count += 1
    
    d[L[i]] += 1
    if d[L[i]] > max:
        max = d[L[i]]

print(max, count)