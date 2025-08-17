'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

'''


def issubsequence(s1, s2):

    n, m = len(s1), len(s2)
    i, j = 0, 0
    while (i < n and j < m):
        if (s1[i] == s2[j]):
            i += 1
        j += 1

    # If i reaches end of s1,that mean we found all
    # characters of s1 in s2,
    # so s1 is subsequence of s2, else not
    return i == n

def isSubsequence_2(s: str, t: str) -> bool:
    m , n = len(s), len(t)
    i, j = 0, 0
    while (i<m and j<n):
        if s[i] == t[j]:
            i += 1
        j += 1

if __name__ == "__main__":
    s1 = "gksrek"
    s2 = "geeksforgeeks"
    if (isSubsequence_2(s1, s2)):
        print("true")
    else:
        print("false")