import pytest
from myCode import longest_palindromic_substring  # Replace 'your_module' with the actual module name

def test_longest_palindromic_substring():
    # Test with standard cases
    assert longest_palindromic_substring("babad") in ["bab", "aba"]
    assert longest_palindromic_substring("cbbd") == "bb"
    
    # Test with empty string
    assert longest_palindromic_substring("") == ""
    
    # Test with single character
    assert longest_palindromic_substring("a") == "a"
    
    # Test with all characters the same
    assert longest_palindromic_substring("aaaaa") == "aaaaa"
    
    # Test with no palindromes longer than 1
    assert longest_palindromic_substring("abcdefg") == "a"

    # Test with special characters
    assert longest_palindromic_substring("ab@ba") == "ab@ba"

