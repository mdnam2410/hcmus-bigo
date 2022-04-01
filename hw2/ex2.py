import numpy as np

def alg(n):
    assignment_count = 2
    comparison_count = 0

    s = 1
    i = 1
    while i < n:
        comparison_count += 1
        j = 1
        while j <= i:
            comparison_count += 1

            s = s + i*j
            j = j + 1
            assignment_count += 2
        comparison_count += 1

        i = 2 * i
        assignment_count += 2
    comparison_count += 1
    return np.array([assignment_count, comparison_count])

def g(n):
    if n == 0 or n == 1:
        return 2
    
    L = np.floor(np.log2(n - 1))
    return 4 * (2**L) + 2*L + 2

def s(n):
    if n == 0 or n == 1:
        return 1
    L = np.floor(np.log2(n - 1))
    return 2 * (2**L) + 2*L + 2

if __name__ == '__main__':
    N = np.arange(0, 1000)
    A = np.array(list(map(alg, N)))

    gs = []
    ss = []

    for n, x in zip(N, A[:, 0]):
        gs.append(g(n) - x)

    for n, x in zip(N, A[:, 1]):
        ss.append(s(n) - x)

    gs = np.array(gs)
    ss = np.array(ss)

    print(f'g(n) is {"correct" if np.all(gs == 0) else "incorrect"}')
    print(f's(n) is {"correct" if np.all(ss == 0) else "incorrect"}')

