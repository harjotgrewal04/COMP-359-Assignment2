# **COMP359-Assignment02: Implememnting Gaussian Elimination in Python**
## **Team Members:**
- Diana Emel
- Tolu Adekore
- Harjot Grewal 

## **Implementing two Gaussian Elimination Algorithms:**
In our group's project we discussed implementing two Gaussian Elimination algorithms where one is naive and the other is not. One of the versions includes partial pivoting while the other does not. The main difference between these two versions is the handling of numbers and how the naive algorithm can run into errors more than the one which includes partial pivoting.


## **Plan & Logging of Work:**
- **Version control:** Git was used to track all contributions. See `git_log.txt`. 
- **Task split:** 
 - **Diana Emal and Harjot Grewal:** Implemented Gaussian Elimination algorithm with partial pivoting, and write a test function to test the algoithm on different systems. 
  - **Tolu Adekore:** Implemented and tested Naive Gaussian Elimination algorithm.
- All members contributed coding, testing, and documentation.

## **Debugging / Testing Code**:
- **Methods used:** verbose print statements, assertions, NumPy result comparison, structured test cases, and timing analysis.  
- **Naive Gaussian Elimination:**  
  - Used detailed print statements (`verbose=True`) to trace each elimination and substitution step.  
  - Included zero-pivot checks and descriptive error messages for easier debugging.  
  - Compared results with `np.linalg.solve()` to assess correctness.  
  - Demonstrated key limitations (zero pivot, instability, lack of pivoting) through test cases.  
- **Partial Pivoting Gaussian Elimination:**  
  - Implemented structured tests with assertions to automatically verify correctness.  
  - Used pivot selection print logs and row-swap outputs for debugging.  
  - Tested performance using `time.perf_counter()` and visualized results using Matplotlib bar charts.  
- **Example test cases:**  
  - Well-conditioned system → correct solution produced.  
  - Zero pivot system → triggers “Zero pivot error” message.  
  - Small pivot system → demonstrates numerical instability.  
  - Random 5×5 system → validated against `np.linalg.solve()`.  
  - Singular system → raises `ValueError` as expected.  
- **Logs:** All printed intermediate matrices, pivot choices, elimination steps, and final results to the console for debugging and verification can be found in `tests` folder.

## **References & Citations:**

- GeeksforGeeks. (n.d.). *Gaussian Elimination to Solve Linear Equations*. GeeksforGeeks. https://www.geeksforgeeks.org/dsa/gaussian-elimination/
-  StudySession. (2023). *Gauss Elimination With Partial Pivoting In Python | Numerical Methods* [Video]. StudySession. https://www.youtube.com/watch?v=DiZ0zSzZj1g
- MIT OpenCourseWare. (n.d.). *Linear Algebra Course Materials*. Massachusetts Institute of Technology. https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/
- SciPy. (n.d.). *Advanced NumPy Tutorial*. SciPy Lecture Notes. https://scipy-lectures.org/advanced/advanced_numpy/
- Rosetta Code. (n.d.). *Gaussian Elimination in Python*. Rosetta Code. https://rosettacode.org/wiki/Gaussian_elimination#Python
- W3Schools. (n.d.). Matplotlib Bars. W3Schools. Retrieved October 18, 2025, from https://www.w3schools.com/python/matplotlib_bars.asp
- Hjelle, G. A. (2024, December 8). Python timer functions: Three ways to monitor your code. Real Python. Retrieved October 18, 2025, from https://realpython.com/python-timer/
- astudentofmaths. (2017, December 6). Why is efficiency of Gaussian Elimination O(n³)? Mathematics StackExchange. Retrieved October 18, 2025, from https://math.stackexchange.com/questions/2554714/why-is-efficency-of-gaussian-elimination-on3
- GeeksforGeeks. (2024, March 8). numpy.argmax() in Python. GeeksforGeeks. Retrieved October 19, 2025, from https://www.geeksforgeeks.org/python/numpy-argmax-python/
- H Harder, D. W. (n.d.). Why Use Partial Pivoting? Department of Electrical and Computer Engineering, University of Waterloo. Retrieved October 19, 2025, from https://ece.uwaterloo.ca/~dwharder/Why_partial_pivoting/
  
