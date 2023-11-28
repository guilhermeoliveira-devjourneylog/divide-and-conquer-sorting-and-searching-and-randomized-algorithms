def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example of usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)

# In this example, we have two functions: merge_sort and merge. The merge_sort function performs recursive
# division of the array until subarrays of size 1 are reached. The merge function takes two sorted subarrays
# and merges them into a new sorted array.

# Execution:

#     Initial Division: [38, 27, 43, 3, 9, 82, 10]
#     Recursive Division: [38, 27, 43], [3, 9, 82, 10], ...
#     Merging: [27, 38, 43], [3, 9, 10, 82], ...
#     Final Result: [3, 9, 10, 27, 38, 43, 82]
