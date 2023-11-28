import math

def distance(p1, p2):
    """
    Calculates the Euclidean distance between two points.
    """
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def brute_force(points):
    """
    Finds the closest pair of points using brute force.
    """
    n = len(points)
    if n < 2:
        return float('inf'), None, None
    
    min_distance = distance(points[0], points[1])
    closest_pair = (points[0], points[1])

    for i in range(n - 1):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    return min_distance, closest_pair[0], closest_pair[1]

def closest_pair_recursive(Px, Py):
    """
    Finds the closest pair of points using a recursive approach.
    """
    n = len(Px)

    # Base Case: Brute Force for few points
    if n <= 3:
        return brute_force(Px)

    mid = n // 2
    Qx = Px[:mid]
    Rx = Px[mid:]

    # Recursive Division
    Qy = sorted([p for p in Py if p in Qx], key=lambda x: x[1])
    Ry = sorted([p for p in Py if p in Rx], key=lambda x: x[1])

    (left_distance, left_point1, left_point2) = closest_pair_recursive(Qx, Qy)
    (right_distance, right_point1, right_point2) = closest_pair_recursive(Rx, Ry)

    # Combine Results
    delta = min(left_distance, right_distance)
    (strip_distance, strip_point1, strip_point2) = closest_pair_in_strip(Py, delta)

    # Final Result
    if strip_distance < delta:
        return strip_distance, strip_point1, strip_point2
    elif left_distance < right_distance:
        return left_distance, left_point1, left_point2
    else:
        return right_distance, right_point1, right_point2

def closest_pair_in_strip(Py, delta):
    """
    Finds the closest pair of points in a central strip.
    """
    n = len(Py)
    min_distance = delta
    best_pair = None

    for i in range(n - 1):
        for j in range(i + 1, min(i + 7, n)):
            dist = distance(Py[i], Py[j])
            if dist < min_distance:
                min_distance = dist
                best_pair = (Py[i], Py[j])

    if best_pair is not None:
        return min_distance, best_pair[0], best_pair[1]
    else:
        # If no pair is found, return a default value
        return float('inf'), None, None

# Example Usage
points = [(0, 0), (1, 1), (2, 2), (3, 3), (5, 5), (7, 7), (9, 9)]
Px = sorted(points, key=lambda x: x[0])
Py = sorted(points, key=lambda x: x[1])

distance, point1, point2 = closest_pair_recursive(Px, Py)

print(f"Closest distance: {distance}")
print(f"Point 1: {point1}")
print(f"Point 2: {point2}")
