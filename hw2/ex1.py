import numpy as np

def alg(n):
    comparison_count = 0
    assignment_count = 2

    s = 0
    i = 0
    while i < n:
        comparison_count += 1
        j = i
        while j <= n - i:
            comparison_count += 1
            s = s + i * j
            j = j + 1
            assignment_count += 2

        i = i + 1
        comparison_count += 1
        assignment_count += 2
    comparison_count += 1

    return np.array([assignment_count, comparison_count])

def g(n):
    if n == 0:
        return 2
    elif n % 2 == 0:
        return 1/2 * (n**2) + 4*n + 4
    else:
        return 1/2 * (n**2) + 4*n + 7/2

def s(n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return 1/4 * (n**2) + 3*n + 2
    else:
        return 1/4 * (n**2) + 3*n + 7/4

if __name__ == '__main__':
    ns = np.arange(0, 500)
    a = np.array(list(map(alg, ns)))

    gs, ss = [], []
    for n, x in zip(ns, a[:, 0]):
        gs.append(g(n) - x)

    for n, x in zip(ns, a[:, 1]):
        ss.append(s(n) - x)

    gs = np.array(gs)
    ss = np.array(ss)

    print(f'g(n) is {"correct" if np.all(gs == 0) else "incorrect"}')
    print(f's(n) is {"correct" if np.all(ss == 0) else "incorrect"}')
    
