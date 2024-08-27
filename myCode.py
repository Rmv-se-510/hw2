
def longest_palindromic_substring(s: str) -> str:
    """
    This function finds and returns the longest palindromic substring within the given input string. 
    It uses a dynamic programming approach to optimize the solution, reducing the time complexity from exponential to polynomial time.

    Arguments:
        s (str): The input string in which to find the longest palindromic substring.

    Returns:
        str: The longest palindromic substring within the input string.

    Time Complexity:
        O(n^2)
    """


    # if the input string is empty then there is no palindromic string
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
    
    lps = s[start:start + max_length]

    return lps