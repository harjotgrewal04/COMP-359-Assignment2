# **Applying Analysis Framework to Gaussian Elimination**

## **Gaussian Eliminiation Rundown**
- Use elementary operations to get matrix into upper-triangular form
- Lower triangle should all be zeroes
- Consistent Independent System has one solution
- Consistent Dependent System has infinite solutions
- Inconsistent System has no solutions
  
## **Algorithm Design Choice**
- Naive Version: Forward Elimination & Back Substitution
- Improved Version: Partial Pivoting, Forward Elimination & Back Substitution
  
## **1. Comparison of Two Versions**

### **1.1 Naive Version**
- Made up of two steps Forward Elimination & Back Substitution
- Poor stability, open to round off errors
- Also open to errors regarding the pivot element & 0

### **1.2 Partial Pivoting**
- Has three steps with an addition of Partial Pivoting
- Has increased stablitity, deals better with round off errors
- Better handling of pivot element

## **2. Performance Analysis**

### **2.1 Naive Gaussian Elimination**
- Time Complexity O(n^3)
- Space Complexity O(n^2)
- Execution time: 0.0007377089932560921 seconds

### **2.2 Partial Pivot Gaussian Elimination**
- Time Complexity O(n^3)
- Space Complexity O(n^2)
- Execution time: 0.04204920801566914 seconds

### **2.3 Analysis of Results**
- Naive gaussian elimination may be a lot quicker than partial pivot gaussian elimination however a lot more unstable
- Both share the same time & space complexity as forward complexity is where the bulk of the operations are to reduce the matrix
