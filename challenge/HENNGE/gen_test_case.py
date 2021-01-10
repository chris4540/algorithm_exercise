import numpy as np

if __name__ == '__main__':
    N = 100
    print(N)
    for _ in range(N):
        nSize = np.random.randint(1, 100)
        print(nSize)
        arr = np.random.randint(-100, 100, size=nSize)
        print(' '.join(map(str, arr)))
