"""
Sorting Module

This module contains a function that implements the selection sort algorithm.
The selection sort algorithm sorts an array by repeatedly finding the minimum 
element from the unsorted part of the array and moving it to the sorted part.
"""

def selection_sort(arr):
    """
    Sorts an array using the selection sort algorithm.
    
    The function iterates over the array, finding the smallest element 
    in the unsorted portion and swapping it with the first unsorted element. 
    It continues this process until the entire array is sorted.
    
    Parameters:
    arr (list): A list of elements to be sorted. The elements must be comparable.

    Returns:
    list: The sorted list in ascending order.

    Example:
    >>> selection_sort([64, 25, 12, 22, 11])
    [11, 12, 22, 25, 64]
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr