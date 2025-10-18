import numpy as np
import time
import matplotlib.pyplot as plt


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
    times = []
    # Test 1: simple system
    A1 = np.array([[2, 1, 1],
                   [1, 3, 2]], dtype=float)
    A1_copy = A1.copy()
    start_time1 = time.perf_counter()
    partial_pivot_gaussian_elimination(A1_copy)
    x1 = back_substitute(A1_copy)
    end_time1 = time.perf_counter()
    elapsed_time1 = end_time1 - start_time1
    expected1 = np.linalg.solve(A1[:, :2], A1[:, 2])
    print("Execution time for Simple Sysytem: ",elapsed_time1)
    times.append(("Simple System", elapsed_time1))
    assert np.allclose(x1, expected1), f"Test 1 failed"


    # Test 2: pivoting needed
    A2 = np.array([[1e-20, 1, 1],
                   [1, 1, 2]], dtype=float)
    A2_copy = A2.copy()
    start_time2 = time.perf_counter()
    partial_pivot_gaussian_elimination(A2_copy)
    x2 = back_substitute(A2_copy)
    end_time2 = time.perf_counter()
    elapsed_time2 = end_time2 - start_time2
    expected2 = np.linalg.solve(A2[:, :2], A2[:, 2])
    print("Execution time for system with needed pivoting: ",elapsed_time2)
    times.append(("Pivoting Needed",elapsed_time2))
    assert np.allclose(x2, expected2), f"Test 2 failed"

    # Test 3: random 5x5 system
    np.random.seed(0)
    n = 5
    A = np.random.rand(n, n)
    b = np.random.rand(n)
    A_aug = np.column_stack((A, b))
    A_aug_copy = A_aug.copy()
    start_time3 = time.perf_counter()
    partial_pivot_gaussian_elimination(A_aug_copy)
    x3 = back_substitute(A_aug_copy)
    end_time3 = time.perf_counter()
    elapsed_time3 = end_time3 - start_time3
    print("Execution time for random 5x5 system: ", elapsed_time3)
    times.append(("Random 5x5 System",elapsed_time3))
    expected3 = np.linalg.solve(A, b)
    assert np.allclose(x3, expected3, atol=1e-10), "Test 3 failed"

    # Test 4: singular system
    A4 = np.array([[1, 2, 3],
                   [2, 4, 6]], dtype=float)
    A4_copy = A4.copy()
    start_time4 = time.perf_counter()
    try:
        partial_pivot_gaussian_elimination(A4_copy)
        x4 = back_substitute(A4_copy)
        assert False, "Test 4 failed"
    except ValueError:
        pass  # expected
    end_time4 = time.perf_counter()
    elapsed_time4 = end_time4 - start_time4
    print("Execution time for a singular system: ", elapsed_time4)
    times.append(("Singular System",elapsed_time4))
    return times
    print("All tests passed ✅")


if __name__ == "__main__":
    times = test_partial_pivot_gaussian_elimination()
    labels, values = zip(*times)

    plt.figure(figsize=(8, 5))
    plt.bar(labels, values)
    plt.title("Partial Pivoting Gaussian Elimination Runtime per Test")
    plt.xlabel("Test Case")
    plt.ylabel("Execution Time (seconds)")
    plt.tight_layout()
    plt.show()
    
