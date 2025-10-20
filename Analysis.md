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
- Naive elimination is not good at handling a zero element in the pivot position
- Partial pivot is a step up from naive elimination but we can improve number stablity even more with scaled partial pivot
- Partial pivot requires a more complex implementation to find the pivot and the swapping of rows

### **1.2 Numerical Stability**
- Naive gaussian elimination is exposed to rounding errors
- Partial pivot avoids smaller pivots to prevent numbers from blowing up.
- Naive gausssian elimination can provide inaccurate results if numbers begin to overflow/underflow
- Partial pivot focuses on numerical stability while naive gaussian focuses on simplifying the elimination process

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

### **2.4 Test Cases**

#### **2.4.1 Naive Gaussian Elimination Cases**
- Used a well-conditioned 3x3 system which executes fine
- Use a system which has a zero in a pivot spot and how this algorithm cannot identify this causing an error
- Used a system with a very small pivot which shows how we get rounding errors when we do not swap rows and divide by very small numbers causing numerical unstability

#### **2.4.2 Partial Pivot Gaussian Elimination Cases**
- Used a simple system to demonstrate the algorithm
- Used a system which needs pivoting with a very small number in the pivot to show how it handles the numerical stabliity
- Uses a random 5x5 system which can handle larger values while providing the same numberical stability
- A singular system which can handle the zero element in a pivot stop which is a major flaw in the naive version

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
To sum up, implementing two different versions of Gaussian Elimination demonstrates all of the scenarios that the partial pivot version can handle which the naive version cannot handle. Although they share both the same time complexity and space complexity only partial pivot elimination can handle numerical stability and prevent round off errors. The naive version may certainly be quicker in its process however can present inaccurate results but fails to handle other things as well like zero pivots which the partial pivot can handle. In a small tradeoff of overhead the partial pivot provides stability and ensure numerical robustness, making it more practical and consistent use. 


