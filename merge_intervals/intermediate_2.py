'''
Given two lists of intervals, find their intersection
'''

def interval_intersection(first_list, second_list):
    result = []
    i, j = 0, 0  # Pointers for both lists

    while i < len(first_list) and j < len(second_list):
        # Find the overlap, if any
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])

        if start <= end:  # Valid intersection
            result.append([start, end])

        # Move the pointer for the interval that ends earlier
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1

    return result

# Example usage
print(interval_intersection([[0, 2], [5, 10], [13, 23], [24, 25]],
                             [[1, 5], [8, 12], [15, 24], [25, 26]]))
# Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
