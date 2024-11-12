"""
Task 1: Identifying Key Operations

Key Operations in Bubble Sort:

1. Outer Loop (for i in range(n)):
    - The outer loop runs from i = 0 to i = n-1, meaning it iterates n times.
    - This loop primarily serves to control the number of iterations over the array. After each pass, the largest unsorted element bubbles up to its correct position, so each pass reduces the size of the unsorted portion of the array by one.
2. Inner Loop (for j in range(0, n-i-1)):
    - The inner loop performs a comparison and possible swap for adjacent elements.
    - The number of iterations of the inner loop depends on the current value of i. On the first pass, the inner loop runs n-1 times, on the second pass it runs n-2 times, and so on. The number of iterations of the inner loop decreases by one after each pass, because the last elements in the array are already in their correct positions.
3. Comparison and Swap (if arr[j] > arr[j+1] and arr[j], arr[j+1] = arr[j+1], arr[j]):
    - The inner loop compares adjacent elements in the array, and if the current element is greater than the next element, it swaps them.

** Key Operations Summary:
    - The outer loop controls the number of passes (iterates n times).
    - The inner loop compares and possibly swaps adjacent elements (iterates up to n-i-1 times).
    - The swap operation occurs whenever two adjacent elements are out of order, which takes constant time O(1).
"""

#--------------------------------------------------------------------------------------------------------------------------------

"""
Task 2: Calculating Big O Complexity

Time Complexity of Bubble Sort:
-------------------------------
The time complexity of Bubble Sort is derived from the two nested loops:
    - Outer loop runs n times (where n is the length of the array).
    - Inner loop runs n-i-1 times for each value of i. On the first iteration (i = 0), the inner loop runs n-1 times; on the second iteration (i = 1), it runs n-2 times, and so on.

The overall time complexity of the algorithm is O(n^2).

Best case: 
    - The input array is already sorted. In this case, Bubble Sort performs n comparisons but no swaps, so the complexity is still O(n^2) in the worst case, but in practice, this can be optimized to O(n) by adding a flag to check if any swaps were made.
Worst case: 
    - The worst case occurs when the array is sorted in reverse order. In this case, the algorithm performs the maximum number of comparisons and swaps. Therefore, the complexity is O(n^2).

Space Complexity:
-----------------
    - The space complexity is O(1), as it only uses a constant amount of additional memory for temporary variables (like the temporary variable used in the swap operation).
"""

#------------------------------------------------------------------------------------------------------------------------------------

"""
Task 3: Efficiency Analysis

Analysis of Bubble Sort's Efficiency:

Time Efficiency:
----------------
    - Bubble Sort is inefficient for large datasets because of its O(n^2) time complexity. As the input size grows, the number of comparisons and swaps grows quadratically, which makes the algorithm unsuitable for large datasets.
    - Best case (O(n)) is possible with a small optimization: if no swaps are made during a pass, the algorithm can terminate early, indicating that the array is already sorted. This improvement reduces the best-case time complexity to O(n) but doesn't help with the worst-case scenario.
    
Space Efficiency:
-----------------
    - Bubble Sort is space-efficient, with a space complexity of O(1). It doesn't require any additional data structures besides the input array, making it a memory-efficient sorting algorithm.

Improvements and Alternative Algorithms:
----------------------------------------
1. Optimized Bubble Sort:
    - Adding a flag to check if any swaps occurred during an inner loop pass can improve the best case to O(n) (early termination).
"""

def optimized_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break

"""
    - In this optimized version, if no swaps are made in a pass (meaning the array is already sorted), the algorithm exits early, improving performance for nearly sorted data.

Alternative Algorithms:
-----------------------
1. Merge Sort (O(n log n)): 
    - Merge Sort is an algorithm that has a better time complexity of O(n log n), which is significantly faster than Bubble Sort for large datasets.
2. Quick Sort (O(n log n)): 
    - Quick Sort is another algorithm that, on average, performs very well with a time complexity of O(n log n). However, it has a worst-case complexity of O(n^2), though this can be mitigated with random pivot selection or other optimizations.
3. Insertion Sort (O(n^2)): 
    - Insertion Sort also has O(n^2) time complexity in the worst case, but it performs well on small or nearly sorted datasets. It may be a better option for smaller arrays compared to Bubble Sort.



Summary of Key Points:
----------------------
1. Key Operations:
    - Outer loop iterates n times.
    - Inner loop iterates n-i-1 times for each i.
    - Comparison and swap (constant time operation) are the core actions of the algorithm.
2. Time Complexity:
    - Best Case: O(n) (if optimized with an early exit on no swaps).
    - Worst Case: O(n^2) (for reverse-ordered input).
    - Overall: O(n^2) due to the nested loops.
3. Space Complexity:
    - O(1) (in-place sorting with no extra space needed).
4. Efficiency Analysis:
    - Bubble Sort is inefficient for large datasets due to its O(n^2) time complexity.
5. Improvements: 
    - Early termination can reduce the best-case time complexity to O(n).
6. Alternatives: 
    - More efficient algorithms like Merge Sort and Quick Sort (both O(n log n)) should be used for larger datasets.

"""