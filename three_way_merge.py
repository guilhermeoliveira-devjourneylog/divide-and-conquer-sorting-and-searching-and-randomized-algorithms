# The 3-way merge sort is a variation of the traditional merge sort where, 
# instead of dividing the array into two halves, it divides 
# it into three thirds. The overall asymptotic running time can be 
# analyzed similarly to the traditional merge sort.

def merge_sort_3way(arr):
    if len(arr) <= 3:
        return sorted(arr)

    third = len(arr) // 3
    left_third = merge_sort_3way(arr[:third])
    middle_third = merge_sort_3way(arr[third:2*third])
    right_third = merge_sort_3way(arr[2*third:])

    return merge_3way(left_third, middle_third, right_third)

def merge_3way(left, middle, right):
    result = []
    i = j = k = 0

    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] < middle[j]:
            if left[i] < right[k]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[k])
                k += 1
        else:
            if middle[j] < right[k]:
                result.append(middle[j])
                j += 1
            else:
                result.append(right[k])
                k += 1

    # Adiciona os elementos restantes, se houver
    result.extend(left[i:])
    result.extend(middle[j:])
    result.extend(right[k:])

    return result

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort_3way(arr)
print("Array original:", arr)
print("Array ordenado:", sorted_arr)
