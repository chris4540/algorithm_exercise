import numpy as np

if __name__ == '__main__':
    num_test = int(input())
    for case in range(1, num_test+1):
        # read the size of the matrix
        n_dim = int(input())
        # allocate the 2d-array for later calculation
        mat = np.zeros((n_dim, n_dim), dtype=np.int)

        # read it line by line
        for i in range(n_dim):
            mat[i, :] = [int(i) for i in input().split()]

        # calculate trace and
        # the number rows and cols containing repeated elements

        # Trace
        trace = np.trace(mat)

        # repeatition
        # method1: hashset
        # method2: sum
        # use method 1

        # rows
        n_rep_rows = 0
        for i in range(n_dim):
            row = mat[i, :]
            if len(set(row)) < n_dim:
                n_rep_rows += 1

        # cols
        n_rep_cols = 0
        for j in range(n_dim):
            col = mat[:, j]
            if len(set(col)) < n_dim:
                n_rep_cols += 1
        print("Case #{}: {} {} {}".format(case, trace, n_rep_rows, n_rep_cols))

