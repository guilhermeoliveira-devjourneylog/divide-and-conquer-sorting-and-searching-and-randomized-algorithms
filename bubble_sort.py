def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        # The last i elements are already sorted, so we don't need to consider them
        for j in range(0, n-i-1):
            # Swap if the current element is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Example Usage
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)

print("Sorted List:", my_list)
