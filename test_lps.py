import warnings
import pytest
from lps.myfile import longest_palindromic_substring

warnings.filterwarnings('ignore')


def test_empty_string():
    """
    Test with empty string
    """

    assert longest_palindromic_substring("") == ""


def test_single_character():
    """
    Test with single character
    """

    assert longest_palindromic_substring("a") == "a"


def test_with_all_characters_same():
    """
    Test with all characters the same
    """

    assert longest_palindromic_substring("aaaaa") == "aaaaa"


def test_with_palindrome_in_list():
    """
    Test if substring in palindrome matches one in list
    """

    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_with_standard_case():
    """
    Test with any standard palindromic string
    """
    assert longest_palindromic_substring("cbbd") == "bb"

    
def test_wih_special_characters():
    """
    Test with special characters
    """

    assert longest_palindromic_substring("ab@ba") == "ab@ba"

   
def test_with_palindromes_with_length_one():
    """
    Test with no palindromes longer than 1
    """

    assert longest_palindromic_substring("abcdefg") == "a"


def test_with_wrong_palindrome_substring():
    """
    Test case with wrong palindromic string
    """

    assert longest_palindromic_substring("abcdefg") == "ab"

    