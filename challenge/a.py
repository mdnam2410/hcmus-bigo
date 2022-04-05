n = int(input())
L = list(map(int, input().split()))

def degenerate(a, i, j, k):
    return a[i] + a[j] <= a[k] or a[i] + a[k] <= a[j] or a[j] + a[k] <= a[i]
        
s = len(L)
for i in range(s):
    for j in range(i+1, s):
        for k in range(j+1, s):
            if not degenerate(L, i, j, k):
                print('YES', sep='')
                exit()
print('NO', sep='')