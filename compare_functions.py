import math

def compare_functions(f1, f2):
    # Fictional function, replace with actual comparison logic
    if f1(1) == f2(1):
        return "equal"
    elif f1(1) < f2(1):
        return "smaller"
    else:
        return "larger"

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

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

# Recurrence: T(n) = 2T(n/2) + O(n)

# Parameters for the Master Theorem:
# A = 2, B = 2, D = 1

# Master Theorem Result:
# T(n) = O(n log n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

# Recurrence: T(n) = 2T(n/2) + O(n)

# Parameters for the Master Theorem:
# A = 2, B = 2, D = 1

# Master Theorem Result:
# T(n) = O(n log n)

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Recurrence: T(n) = T(n-1) + O(1)

# Parameters for the Master Theorem:
# A = 1, B = 1, D = 0

# Master Theorem Result:
# T(n) = O(n)

def merge_sort_analysis(n):
    # Recurrence for Merge Sort
    if n <= 1:
        return 0  # Base case, constant work
    else:
        return 2 * merge_sort_analysis(n/2) + n  # Two recursive calls and linear work outside them

# Parameters for the Master Theorem
a = 2
b = 2
f_n = lambda n: n  # Linear work function

# Comparison with n^log_b(a)
comparison_result = compare_functions(f_n, lambda n: n**(math.log(a, b)))

# Determine complexity based on the comparison
if comparison_result == "equal":
    print("Complexity: Theta(n log n)")
elif comparison_result == "smaller":
    print("Complexity: Theta(n^log_b(a))")
else:
    print("Complexity: Theta(f(n))")

# If comparison_result == "equal":
#     Meaning: This indicates that the actual work function f(n) is asymptotically equal to the theoretical function n^log_b(a).
#     Implication for Complexity: The complexity of the algorithm is Θ(n log n), meaning that the algorithm's efficiency is primarily determined by the function n^log_b(a).

# If comparison_result == "smaller":
#     Meaning: This indicates that the actual work function f(n) is asymptotically smaller than the theoretical function n^log_b(a).
#     Implication for Complexity: The complexity of the algorithm is Θ(f(n)), meaning that the actual work function dominates the performance of the algorithm. The term n^log_b(a) is a "stronger" upper bound than the actual function.

# If comparison_result is another value:
#     Meaning: This indicates that the actual work function f(n) is asymptotically larger than the theoretical function n^log_b(a).
#     Implication for Complexity: The complexity of the algorithm is Θ(f(n)), where the actual work function dominates performance. The term n^log_b(a) is not a "sufficiently strong" upper bound to describe the efficiency of the algorithm.
