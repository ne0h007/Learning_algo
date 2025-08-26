def is_anagram(s, t):
    # If lengths are different, return False
    if len(s) != len(t):
        return False

    # Create a frequency array for 26 lowercase letters
    count = [0] * 26

    # Increment counts for s and decrement counts for t
    for char1, char2 in zip(s, t):
        count[ord(char1) - ord('a')] += 1
        count[ord(char2) - ord('a')] -= 1

    # If all counts are zero, it's a valid anagram
    return all(x == 0 for x in count)

# Example usage
s = "anagram"
t = "nagaram"
print(is_anagram(s, t))  # Output: True

s = "rat"
t = "car"
print(is_anagram(s, t))  # Output: False