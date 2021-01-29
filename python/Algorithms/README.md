# This document covers Algorithms

## Note From MIT

> What Do Computer Scientists Do?
> They think computationally
> Abstractions
> - Choosing the right abstractions
> - Operating in multiple layers of abstractions simultaneously
> - Defining
> algorithms, automated execution

Algorithm - instructions that are used to accomplish a task.

## Binary Search or bisection search

- An algorithm that takes a sorted list.
- Starts in the middle of the list and determines if the mid index is higher or lower.
- If the item is higher than the mid index, you only use the highest half of the list.
- If the item is lower than the mid index, you only use the lower half of the list.
- And then you repeat the midpoint process of the list
- If not found return null.
- NOTE: Through each iteration you get rid of half of the list.
- Another NOTE: Sorted search is never less expensive than linear cost

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

## Linear Search 

- Brute force search
- Check every item in a list until you find what you are looking for
- List does not have to be sorted
- Linear is the worst case because of complexity. You may have to search every item in a list.

### Unsorted Example

```python
def linear_search(list, item):
    found = False
    for i in range(len(list)):
        if item == list[i]:
            found = True
    return found
```

### Sorted Example

- Search through the list if item is greater than i than item is not in list

```python
def linear_search(list, item):
    for i in range(len(list)):
        if list[i] == item:
            return True
        if list[i] > item:
            return False
    return found
```

- One thing we should mention is sorting

## Bubble Sort

- Compares consecutive pairs of elements in a list
- As it compares elements it swaps and places the smallest element first
- Does this swap until it repeats through the list with no swaps

[9, 8, 10, 7]
[8, 9, 10, 7]
[8, 9, 7, 10]
[8, 7, 9, 10]
[7, 8, 9. 10]

### Bubble Sort Example

```python
def bubble_sort(L):
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                temp = L[j]
                L[j] = L[j-1]
                L[j-1] = temp
```

## Merge Sort

- Best worst case algorithm
- Divide and conquer
- Split list in half until you have sublists of only 0,1 element
- Then you merge them and sort
- Repeat this process until you have one sorted list
- Takes less time

### Merge Sort Example

| List 1            | List 2           | Compare       | Result                     |
| :-------------:   | :-------------:  |:-------------:|:-------------:             |
| [1,5,10,13,14,15] | [3,6,9,11]       | [1,3]         | []                         |
| [5,10,13,14,15]   | [3,6,9,11]       | [5,3]         | [1]                        |
| [5,10,13,14,15]   | [6,9,11]         | [5,6]         | [1,3]                      |
| [10,13,14,15]     | [6,9,11]         | [10,6]        | [1,3,5]                    |
| [10,13,14,15]     | [9,11]           | [10,9]        | [1,3,5,6]                  |
| [10,13,14,15]     | [11]             | [10,11]       | [1,3,5,6,9]                |
| [13,14,15]        | [11]             | [13,11]       | [1,3,5,6,9,10]             |
| [13,14,15]        | []               | [13]          | [1,3,5,6,9,10,11]          |
| []                | []               | []            | [1,3,5,6,9,10,11,13,14,15] |

```python
def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left[i]) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    return result

def merge_sort(my_list):
    print('merge sort: ' + str(L))
    if len(my_list) < 2:
        return my_list[:]
    else:
        middle = len(my_list) // 2
        left = merge_sort(my_list[:middle])
        right = merge_sort(my_list[middle:])
        return merge(left, right)
```
