CECS 328 PA2: Tree Grinder Sum Calculator

Testing Procedure:
1. Enter the number of grinders (a positive integer)
2. Enter a list of trees (positive integers) separated by spaces. Must be greater than or equal to number of grinders.
3. Program will output your inputs and the maximum sum of contiguous trees.

*If any invalid input (non-positive integer) is entered, while / if loops will prompt input until valid.

================================Test Case 1================================

Input:
    Enter number of grinders: 3
    Enter tree heights separated by spaces: 2 5 3 10 7
Expected output:
    Tree heights: [2, 5, 3, 10, 7]
    Grinders: 3
    Maximum sum of trees that can be processed: 20 (3 + 10 + 7)

================================Test Case 2================================

Input:
    Enter number of grinders: 5
    Enter tree heights separated by spaces: 5 7 5 3 2 15 2 1
Expected output:
    Tree heights: [5, 7, 5, 3, 2, 15, 2, 1]
    Grinders: 5
    Maximum sum of trees that can be processed: 30 (7 + 5 + 3 + 2 + 15)

================================Test Case 3================================
Input:
    Enter number of grinders: 3
    Enter tree heights separated by spaces: 5 10
Expected output:
    Error: Enter at least 3 trees.
    Loops...
