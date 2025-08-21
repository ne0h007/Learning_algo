# Given schedules of multiple employees, find the time intervals where all employees are free.


import heapq

def employee_free_time(schedule):
    events = []
    for employee_intervals in schedule:
        for interval in employee_intervals:
            events.append((interval[0], 'start'))
            events.append((interval[1], 'end'))

    # Sort events by time, where 'end' events have priority over 'start' events
    events.sort(key=lambda x: (x[0], x[1] == 'start'))

    free_time = []
    prev_time = None
    active_intervals = 0

    # Iterate through sorted events
    for time, event in events:
        if active_intervals == 0 and prev_time is not None and prev_time != time:
            free_time.append([prev_time, time])

        # Update active intervals
        if event == 'start':
            active_intervals += 1
        else:
            active_intervals -= 1

        prev_time = time

    return free_time

# Example usage
print(employee_free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))  # Output: [[3, 4]]

