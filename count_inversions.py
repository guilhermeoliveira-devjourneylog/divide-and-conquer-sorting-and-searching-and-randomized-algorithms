def count_inversions(arr):
    # Main function that counts inversions in an array
    if len(arr) <= 1:
        return arr, 0  # If the array has size 0 or 1, there are no inversions

    # Divide the array in half
    mid = len(arr) // 2
    left, inv_left = count_inversions(arr[:mid])
    right, inv_right = count_inversions(arr[mid:])

    # Merge and count split inversions
    merged, split_inversions = merge_and_count_split_inversions(left, right)

    # Return the sorted array and the total inversions
    return merged, inv_left + inv_right + split_inversions

def merge_and_count_split_inversions(left, right):
    # Merge two sorted arrays and count split inversions
    merged = []
    count = 0  # Counter for split inversions

    i, j = 0, 0  # Indices to traverse the left and right arrays

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            # Count split inversions
            count += len(left) - i
            j += 1

    # Add remaining elements if any
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, count

# Example
input_array = [3, 1, 2, 4, 6, 5]
sorted_array, inversions = count_inversions(input_array)

print("Original array:", input_array)
print("Sorted array:", sorted_array)
print("Number of inversions:", inversions)
