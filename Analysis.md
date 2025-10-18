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

### **2.1 
