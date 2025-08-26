# vertical scanning

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Iterate character-by-character through the first string
    for i in range(len(strs[0])):
        char = strs[0][i]  # Character in the first string
        for string in strs[1:]:
            # Check if index `i` is out of bounds or if characters mismatch
            if i >= len(string) or string[i] != char:
                return strs[0][:i]  # Return the prefix up to this point
    return strs[0]  # If no mismatch, return the full first string

# Example usage
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  # Output: ""


#horizantal scanning
def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Start with the first string as the common prefix
    common_prefix = strs[0]
    
    for i in range(1, len(strs)):
        while strs[i].find(common_prefix) != 0:  # Reduce common_prefix until it matches
            common_prefix = common_prefix[:-1]  # Remove last character
            if not common_prefix:
                return ""  # No common prefix

    return common_prefix

# Example usage
strs = ["flower", "flow", "flight"]
print(longest_common_prefix(strs))  # Output: "fl"

strs = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))  # Output: ""