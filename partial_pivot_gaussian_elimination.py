import numpy as np

def partial_pivot_gaussian_elimination(A):
    n = len(A)  # number of rows

    for i in range(n):
        pivot_row = i
        # find pivot (largest abs in column)
        for j in range(i + 1, n):
            if abs(A[pivot_row][i]) < abs(A[j][i]):
                pivot_row = j
        print(f"Pivot for column {i}: row {pivot_row}")

        # swap rows if pivot changed
        if pivot_row != i:
            A[[i, pivot_row]] = A[[pivot_row, i]]
            print(f"Swapped row {i} with row {pivot_row}:\n{A}")

        # eliminate entries below pivot
        for j in range(i+1, n):
            factor = A[j][i] / A[i][i]
            A[j] -= factor * A[i]
            print(f"Eliminating row {j}, factor {factor}:\n{A}")


def back_substitute(A):
    n = len(A)
    x = np.zeros(n)  # solution vector

    for i in reversed(range(n)):
        if A[i, i] == 0:
            raise ValueError("Singular matrix")
        sum_value = 0
        # sum of known terms
        for j in range(i+1, n):
            sum_value += A[i][j] * x[j]
        x[i] = (A[i][n] - sum_value) / A[i][i]
        print(f"x[{i}] = {x[i]}")

    print("Final solution vector:", x)
    return x


def test_partial_pivot_gaussian_elimination():
    # Test 1: simple system
    A1 = np.array([[2, 1, 1],
                   [1, 3, 2]], dtype=float)
    A1_copy = A1.copy()
    partial_pivot_gaussian_elimination(A1_copy)
    x1 = back_substitute(A1_copy)
    expected1 = np.linalg.solve(A1[:, :2], A1[:, 2])
    assert np.allclose(x1, expected1), f"Test 1 failed"

    # Test 2: pivoting needed
    A2 = np.array([[1e-20, 1, 1],
                   [1, 1, 2]], dtype=float)
    A2_copy = A2.copy()
    partial_pivot_gaussian_elimination(A2_copy)
    x2 = back_substitute(A2_copy)
    expected2 = np.linalg.solve(A2[:, :2], A2[:, 2])
    assert np.allclose(x2, expected2), f"Test 2 failed"

    # Test 3: random 5x5 system
    np.random.seed(0)
    n = 5
    A = np.random.rand(n, n)
    b = np.random.rand(n)
    A_aug = np.column_stack((A, b))
    A_aug_copy = A_aug.copy()
    partial_pivot_gaussian_elimination(A_aug_copy)
    x3 = back_substitute(A_aug_copy)
    expected3 = np.linalg.solve(A, b)
    assert np.allclose(x3, expected3, atol=1e-10), "Test 3 failed"

    # Test 4: singular system
    A4 = np.array([[1, 2, 3],
                   [2, 4, 6]], dtype=float)
    A4_copy = A4.copy()
    try:
        partial_pivot_gaussian_elimination(A4_copy)
        x4 = back_substitute(A4_copy)
        assert False, "Test 4 failed"
    except ValueError:
        pass  # expected

    print("All tests passed ✅")


if __name__ == "__main__":
  
    test_partial_pivot_gaussian_elimination()
