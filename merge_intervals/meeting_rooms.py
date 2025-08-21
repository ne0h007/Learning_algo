# Check if All Meetings Can Be Attended
def can_attend_meetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort by start time
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:  # If overlapping
            return False
    return True

# Example usage
print(can_attend_meetings([[0, 30], [5, 10], [15, 20]]))  # Output: False

# Find Minimum Meeting Rooms Required

def min_meeting_rooms(intervals):
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])

    rooms = 0
    end_pointer = 0

    for start in start_times:
        if start < end_times[end_pointer]:  # Need a new room
            rooms += 1
        else:  # Reuse a room
            end_pointer += 1

    return rooms

# Example usage
print(min_meeting_rooms([[0, 30], [5, 10], [15, 20]]))  # Output: 2