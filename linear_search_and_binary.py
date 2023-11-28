import time

# Linear Search (O(n)):
# Linear search iterates through each element of a list until it finds the desired element.

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return the index
    return -1  # Element not found

# Binary Search (O(log n)):
# Binary search is efficient for sorted lists, repeatedly dividing the list in half until it finds the desired element.

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid  # Element found, return the index
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Element not found

# Create a sorted list
sorted_list = list(range(1, 1000001))

# Define the element we want to find
target_element = 888888

# Perform linear search
start_time = time.time()
linear_result = linear_search(sorted_list, target_element)
linear_time = time.time() - start_time

# Perform binary search
start_time = time.time()
binary_result = binary_search(sorted_list, target_element)
binary_time = time.time() - start_time

# Display the results
print("Sorted list:", sorted_list)
print("Target element:", target_element)
print("Linear Search - Result:", linear_result, "| Time:", linear_time)
print("Binary Search - Result:", binary_result, "| Time:", binary_time)
