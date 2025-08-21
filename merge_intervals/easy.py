def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort the intervals by their start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]  # Initialize with the first interval

    # Step 2: Iterate through the intervals
    for i in range(1, len(intervals)):
        current = intervals[i]
        last_merged = merged[-1]

        # Check for overlap
        if current[0] <= last_merged[1]:  # Overlapping intervals
            last_merged[1] = max(last_merged[1], current[1])  # Merge them
        else:
            merged.append(current)  # No overlap, add to merged list

    return merged

# Example usage
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]