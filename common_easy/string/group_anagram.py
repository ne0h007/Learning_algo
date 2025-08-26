from collections import defaultdict

def group_anagrams(strs):
    # Dictionary to store grouped anagrams
    anagrams = defaultdict(list)

    for word in strs:
        # Create a frequency count of 26 letters (assuming lowercase English letters)
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1  # Map 'a' to index 0, 'b' to index 1, ..., 'z' to index 25

        # Use tuple of the count array as the key (tuples are hashable in Python)
        anagrams[tuple(count)].append(word)

    # Return the grouped values as a list of lists
    return list(anagrams.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))  # Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]