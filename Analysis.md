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

### **1.1 Algorithm Limitations**
- Partial pivoting has better and more accurate treatment of numerical values
- Pivoting helps with rounding error 
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
- Both share the same time & space complexity as forward elimination is where the bulk of the operations are to reduce the matrix
- Naive gaussian elimination is a lot more susceptible to error
- Partial pivoting adds a slight constant overhead

## **3. Design Choices**

### **3.1 Using different matrix variations**
- Allows to show more use cases and better demonstrations of how the algorithmm handles various sizes
- Explains the differences in systems where one may succeed while the other fails

### **3.2 Why use a more complicated algorithm?**
- Has better stability
- Handles rounding erros better & can deal with pivot elements
- Provides more benefits while holding the same time complexity

### **3.3 Timing different matrix systems**
- Allows to see the difference in timing of larger and smaller scale systems
- Shows difference when ran on different hardware systems

## **4. Future Improvements**

### **4.1 Possible Enhancements**
- Adding user input, so a user can input a matrix of their desire
- Take in equations instead of numbers, allows for easier user entry

### **4.2 Performance Optimization**
- Use a faster pivot search like using something built in like argmax
- Use Scaled Partial Pivoting for even greater numerical stability 

## **5. Conclusion**




