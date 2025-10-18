# naive_gaussian.py
import numpy as np
import time

def gaussian_elimination_naive(A, b, verbose=True):
    """
    NAIVE GAUSSIAN ELIMINATION
    Basic implementation without pivoting or numerical safeguards
    Demonstrates critical limitations of simple approach
    """
    n = len(b)
    A = A.astype(float).copy()
    b = b.astype(float).copy()
    
    if verbose:
        print("🔹 NAIVE GAUSSIAN ELIMINATION")
        print("=" * 50)
        print("Initial system:")
        print_matrix_system(A, b)
    
    # Forward elimination
    for i in range(n):
        if verbose:
            print(f"\n🎯 Step {i+1}: Pivot at position ({i},{i}) = {A[i,i]:.10f}")
        
        # CRITICAL FLAW 1: No zero pivot checking
        if abs(A[i,i]) < 1e-15:
            if verbose:
                print(f"❌ CRITICAL ERROR: Zero pivot at position ({i},{i})!")
                print("   Division by zero inevitable - Algorithm fails!")
            return None, "Zero pivot error"
        
        # CRITICAL FLAW 2: No pivoting for numerical stability
        for j in range(i+1, n):
            factor = A[j,i] / A[i,i]  # Direct division - error amplification!
            if verbose:
                print(f"   Eliminating row {j}: factor = {A[j,i]:.6f}/{A[i,i]:.6f} = {factor:.6f}")
            
            # Update entire row
            A[j,i:] = A[j,i:] - factor * A[i,i:]
            b[j] = b[j] - factor * b[i]
            
            if verbose:
                print(f"   Updated system:")
                print_matrix_system(A, b)
    
    if verbose:
        print(f"\n✅ Forward elimination completed")
        print("Upper triangular system:")
        print_matrix_system(A, b)
    
    # Back substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]
        if verbose:
            print(f"   x[{i}] = ({b[i]:.6f} - {np.dot(A[i,i+1:], x[i+1:]):.6f}) / {A[i,i]:.6f} = {x[i]:.6f}")
    
    return x, "Success"

def print_matrix_system(A, b):
    """Helper function to print the augmented matrix nicely"""
    n = len(b)
    for i in range(n):
        row_str = "   ["
        for j in range(n):
            row_str += f"{A[i,j]:8.4f}"
        row_str += f" | {b[i]:8.4f}]"
        print(row_str)

def test_naive_version():
    """Test the naive Gaussian elimination on various cases"""
    print("🧪 TESTING NAIVE GAUSSIAN ELIMINATION")
    print("=" * 60)
    
    # Test 1: Well-conditioned system (should work)
    print("\n1. WELL-CONDITIONED SYSTEM:")
    A1 = np.array([[4, 1, 2],
                   [3, 5, 1],
                   [1, 1, 3]])
    b1 = np.array([4, 7, 3])
    
    x_naive1, status1 = gaussian_elimination_naive(A1, b1)
    print(f"Result: {x_naive1} - Status: {status1}")
    print(f"NumPy reference: {np.linalg.solve(A1, b1)}")
    
    # Test 2: Zero pivot (should fail)
    print("\n2. ZERO PIVOT SYSTEM:")
    A2 = np.array([[0, 2, 3],
                   [1, 4, 5], 
                   [2, 5, 7]])
    b2 = np.array([8, 15, 22])
    
    x_naive2, status2 = gaussian_elimination_naive(A2, b2)
    print(f"Result: {x_naive2} - Status: {status2}")
    
    # Test 3: Small pivot (numerical instability)
    print("\n3. SMALL PIVOT SYSTEM:")
    A3 = np.array([[1e-10, 1, 1],
                   [1, 1, 2],
                   [1, 2, 1]])
    b3 = np.array([1 + 1e-10, 4, 4])
    
    x_naive3, status3 = gaussian_elimination_naive(A3, b3, verbose=False)
    print(f"Result: {x_naive3} - Status: {status3}")
    
    if x_naive3 is not None:
        exact = np.linalg.solve(A3, b3)
        error = np.linalg.norm(x_naive3 - exact)
        print(f"Error vs NumPy: {error:.2e}")

def demonstrate_limitations():
    """Demonstrate the key limitations of naive Gaussian elimination"""
    print("\n\n🔍 KEY LIMITATIONS OF NAIVE VERSION:")
    print("=" * 60)
    
    limitations = [
        "1. ZERO PIVOT FAILURE: Cannot handle zero diagonal elements",
        "2. NUMERICAL INSTABILITY: Small pivots amplify rounding errors", 
        "3. NO PIVOTING: Cannot rearrange rows to find better pivots",
        "4. POOR ERROR HANDLING: Fails catastrophically on many systems",
        "5. ACCUMULATED ERRORS: Repeated operations increase floating-point errors"
    ]
    
    for limitation in limitations:
        print(f"   {limitation}")

if __name__ == "__main__":
    start_time = time.perf_counter()
    test_naive_version()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print("Execution Time: ", elapsed_time)
    demonstrate_limitations()