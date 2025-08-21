'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

 

Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

'''


def maxVowels(s: str, k: int) -> int:
    max_vowel=0
    res =0
    for i in range(0,len(s)):
        if i>=k :
            if s[i-k] in ['a','e','i','o','u']:
                res -=1
        if s[i] in['a','e','i','o','u']:
            res+=1
        max_vowel = max(max_vowel,res)
        if max_vowel ==k:
            return max_vowel
    return max_vowel

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        # Maximum vowels i.e. ans
        ans: int = 0
            
        # Vowels in current window
        currCount: int = 0
            
        # String of vowels
        vowels: str = "aeiou"
            
        # Using sliding window technique to 
        # calculate number of vowels in each window and 
        # update the count
        for i, v in enumerate(s):
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            if s[i] in vowels:
                currCount += 1
            ans = max(currCount, ans)
        return ans
    
