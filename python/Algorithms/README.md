# This document covers Algorithms

Algorithm - instructions that are used to accomplish a task.

## Binary Search

An algorithm that takes a sorted list. Starts in the middle of the list and determines if the mid index is higher or lower and then cuts the list in 1/2 and repeats this process until you are left with one.  the position or returns null.

To understand binary search you need to understand `Logarithms`

- Logs are the flip of exponents

10^2 = 100 <--> log10 100 = 2
10^3 = 1000 <--> log10 1000 = 3

### Example

```python

my_list = [0, 1, 9, 10, 20, 50]
           L     M           U


def binary_search(my_list, item):
    low_index = 0
    high_index = len(my_list) - 1
    while low <= high:
        for i in range(my_list, low_index, )
        # Uses the floor division operator
        # to divide by 2 and rounds down automatically if not an even number
        mid_index = (low_index + high_index) // 2
        # Sets guess to the index number in the list
        guess = my_list[mid_index]
        # if guess equals item return item
        if guess == item:
            return mid_index
        # Skips if guess is less than item
        if guess > item:
            high_index = mid_index -1
        # Your guess was too low
        else:
            low_index = mid_index + 1
    return None
```
