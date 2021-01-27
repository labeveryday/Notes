# This document covers Algorithms

Algorithm - instructions that are used to accomplish a task.

## Binary Search

An algorithm that takes a sorted list. Starts in the middle of the list and determines if its higher or lower and then cuts the list in 1/2 and repeats this process until you are left with one.  the position or returns null.

To understand binary search you need to understand `Logarithms`

- Logs are the flip of exponents

10^2 = 100 <--> log10 100 = 2
10^3 = 1000 <--> log10 1000 = 3

### Example

```python
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    # Uses the floor division operator
    # to divide by 2 and rounds down automatically if not an even number
    mid = (low + high) // 2
    guess = list[mid]
    # if guess is too low update
    if guess < item:
        low = mid + 1
```
