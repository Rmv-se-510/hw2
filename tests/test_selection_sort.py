import warnings
import pytest
import sys
import os

sys.path.append(os.path.join(os.getcwd()))
sys.path.append(os.path.join(os.getcwd(), "sorting_algorithms"))

from sorting_algorithms.selectionSort import selection_sort


warnings.filterwarnings('ignore')

def test_large_array():
    """
    Test with a large array which contains 10 elements
    """
    large_array = [100, 24, 56, 12, 98, 3, 67, 45, 29, 88]
    assert selection_sort(large_array) == sorted(large_array)

def test_array_with_duplicates():
    """
    Test with aa array which contains duplicate elements
    """
    array_with_duplicates = [4, 2, 2, 8, 4, 6, 1, 9, 1]
    assert selection_sort(array_with_duplicates) == sorted(array_with_duplicates)

def test_negative_numbers():
    """
    Test with a large array which contains negative elements
    """
  
    array_with_negatives = [-5, -1, -10, 3, 0, 7, -3]
    assert selection_sort(array_with_negatives) == sorted(array_with_negatives)

def test_mixed_positive_negative():
    """
    Test with a large array which contains mixed elements (positive & negative)
    """
  
    mixed_array = [15, -3, 22, -1, 0, 6, -9, 8]
    assert selection_sort(mixed_array) == sorted(mixed_array)

def test_floats_and_integers():
    """
    Test with a large array which contains float & int type of elements
    """
  
    mixed_float_int_array = [4.5, 2, 9.3, 1, 7.8, 0, 3]
    assert selection_sort(mixed_float_int_array) == sorted(mixed_float_int_array)