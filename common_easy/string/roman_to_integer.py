def roman_to_int(s):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        # Check if the next numeral is larger (subtraction case)
        if i < n - 1 and roman_values[s[i]] < roman_values[s[i + 1]]:
            total -= roman_values[s[i]]
        else:
            total += roman_values[s[i]]
    
    return total

# Example usage
print(roman_to_int("III"))     # Output: 3
print(roman_to_int("LVIII"))   # Output: 58
print(roman_to_int("MCMXCIV")) # Output: 1994