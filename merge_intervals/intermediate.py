''' 
In this problem, we are given a list of non-overlapping intervals and a new interval. We need to  merge the new interval into the list, preserving order and merging any overlaps.
'''

def insert_interval(intervals, new_interval):
    result = []
    for interval in intervals:
        # Case 1: No overlap and the interval is before new_interval
        if interval[1] < new_interval[0]:
            result.append(interval)
        # Case 2: No overlap and the interval is after new_interval
        elif interval[0] > new_interval[1]:
            result.append(new_interval)
            new_interval = interval
        # Case 3: Overlapping intervals
        else:
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
            
    result.append(new_interval)
    return result

# Example usage
print(insert_interval([[1, 3], [6, 9]], [2, 5]))  # Output: [[1, 5], [6, 9]]