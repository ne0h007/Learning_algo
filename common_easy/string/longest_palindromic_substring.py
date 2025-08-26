def longest_palindromic_substring(s):
    # Preprocess the string to avoid even/odd length problems
    t = "#" + "#".join(s) + "#"
    n = len(t)
    p = [0] * n  # Array to store the palindrome radius at each index
    center = 0
    right = 0

    for i in range(1, n - 1):
        mirror = 2 * center - i  # Mirror index of i with respect to the center

        if i < right:
            p[i] = min(right - i, p[mirror])  # Use symmetry to get initial p[i]

        # Expand around i while it's a palindrome
        while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        # Update center and right boundary if the palindrome expands past `right`
        if i + p[i] > right:
            center = i
            right = i + p[i]

    # Find the maximum palindrome length and its center
    max_len = max(p)
    center_index = p.index(max_len)
    start = (center_index - max_len) // 2  # Map the center index back to the original string
    return s[start:start + max_len]

# Example usage
s = "babad"
print(longest_palindromic_substring(s))  # Output: "bab" or "aba"