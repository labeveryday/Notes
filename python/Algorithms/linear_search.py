"""
Linear searches iterate through an entire list and return the value
"""

position = -1

def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['position'] = i
            return True
    return False


my_list = [1, 4, 7, 2, 10, 99, 3, 8, 6]

results = search(my_list, 4)

print(f"Whats number in list: {results} and num is {position}")
