Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1), since it takes exactly 1 step to complete the append function. 

2. What is the space complexity of your ring buffer's `append` function?

O(1), since we only need to devote size 1 space to complete the append function. 

3. What is the runtime complexity of your ring buffer's `get` method?

O(n), since we are looping through each item in the length of the capacity of the storage.  

4. What is the space complexity of your ring buffer's `get` method?

O(n), since the for loop is increasing the size of the memory needed by each iTh iteration, thus increasing the byte size.  

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2), since there are two nested for loops. 

6. What is the space complexity of the provided code in `names.py`?

O(n), since the for loop is increasing the size of the memory needed, per each nTh iteration. This increases the required bytes needed.  

7. What is the runtime complexity of your optimized code in `names.py`?

Since we are applying binary search tree for each item name, the step size will be n * log(n), log(n) representing the BST, and n representign the names in name_1. Thus, O(n*log(n))

8. What is the space complexity of your optimized code in `names.py`?

log(n), since the binary search tree is reducing the amount of names needed to be placed in the memory.  

