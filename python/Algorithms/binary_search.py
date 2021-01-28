
locations = []
with open('locations.txt', 'r') as f:
    for location in f:
        locations.append(location.split(',')[0])


locations = sorted(locations)

def binary_search(list, item):
    i = 0
    low = 0
    high = len(list) - 1
    while low <= high:
        i += 1
        # Uses the floor division operator
        # to divide by 2 and rounds down automatically if not an even number
        mid = (low + high) // 2
        guess = list[mid]
        # if guess equals item return item
        if guess == item:
            return f"{list[mid]} at position {mid} \n In {i} steps"
        # Your guess is too high
        if guess > item:
            high = mid -1
        # Your guess was too low
        else:
            low = mid + 1
    return None

 
