# longest_palindromic_substring.py

def longest_palindromic_substring(s: str) -> str:
    n = len(s)
    if n == 0:
        return ""
    
    # Table to store palindromic substrings
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_length = 1
    
    # All substrings of length 1 are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for palindromes of length 2
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check for palindromes of length greater than 2
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                start = i
                max_length = length
    
    return s[start:start + max_length]

# Predefined inputs with expected outcomes
test_cases = [
    ("babad", "aba"),       # Both "aba" and "bab" are valid, but only one is expected here
    ("cbbd", "bb"),         # Correct
    ("a", "a"),             # Correct
    ("", ""),               # Correct
    ("aaaaa", "aaaaa"),     # Correct
    ("ab@ba", "ab@ba"),     # Correct

    # Test cases expected to fail (intentionally incorrect results)
    ("racecar", "aceca"),   # Expected "racecar", but set to "aceca"
    ("madam", "ada"),       # Expected "madam", but set to "ada"
    ("level", "eve"),       # Expected "level", but set to "eve"
    ("noon", "oo"),         # Expected "noon", but set to "oo"
    ("abcba", "bcb")        # Expected "abcba", but set to "bcb"
]

# Running the function on predefined inputs
for test_string, expected in test_cases:
    result = longest_palindromic_substring(test_string)
    print(f"Input: {test_string}")
    print(f"Longest Palindromic Substring: {result}")
    print(f"Expected: {expected}")
    print("Test Passed" if result == expected else "Test Failed")
    print()
