# Find the smallest substring in s that contains all the characters from string t.

from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""

    t_count = Counter(t)
    window_count = {}
    required = len(t_count)
    formed = 0

    left, right = 0, 0
    min_len = float('inf')
    min_window = (0, 0)

    while right < len(s):
        char = s[right]
        window_count[char] = window_count.get(char, 0) + 1
        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                formed -= 1
            left += 1

        right += 1

    left, right = min_window
    return s[left:right+1] if min_len != float('inf') else ""

# Example usage
print(min_window("ADOBECODEBANC", "ABC"))  # Output: "BANC"