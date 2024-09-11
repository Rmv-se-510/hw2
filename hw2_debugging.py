"""
This module contains functions for array manipulation, including
merging arrays (merge sort) and generating arrays filled with random values.
The functions implemented in this module include:
- merge_sort
- recombine
"""
import rand


def merge_sort(arr):
    """
    Perform the merge sort algorithm on a list of elements.

    Merge sort is a divide-and-conquer algorithm that splits the input list
    into smaller sublist, sorts each sublist, and then merges the sorted
    sublist to produce the final sorted list.

    Time Complexity:
        - Best: O(n log n)
        - Average: O(n log n)
        - Worst: O(n log n)

    Space Complexity:
        - O(n) due to the temporary arrays used during the merging process.

    Args:
        arr (list): The list of elements to be sorted. The elements must be
                    comparable, i.e., they should support comparison operators.

    Returns:
        list: A new list containing the elements of `arr`, sorted in
        ascending order.

    Example:
        merge_sort([3, 1, 4, 1, 5, 9, 2, 6])
        [1, 1, 2, 3, 4, 5, 6, 9]
    """
    if len(arr) == 1:
        return arr

    half = len(arr)//2

    return recombine(merge_sort(arr[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
    Merge two sorted arrays (left_arr and right_arr) into a single sorted
    array. This function takes two sorted arrays as input and combines them
    into one sorted array by comparing elements from both arrays and
    placing the smaller element in the correct position of the resulting
    array. It handles any remaining elements after one array is exhausted
    by appending them to the result.

    Args:
        left_arr (list): The first sorted array.
        right_arr (list): The second sorted array.

    Returns:
        list: A new list containing the elements from both
        `left_arr` and `right_arr`, sorted in ascending order.

    Example:
        recombine([1, 3, 5], [2, 4, 6])
        [1, 2, 3, 4, 5, 6]
    Notes:
        - Assumes both `left_arr` and `right_arr` are individually sorted.
        - The resulting array will be of size `len(left_arr) + len(right_arr)`.

    """
    left_index = 0
    right_index = 0
    temp_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr[temp_index] = left_arr[left_index]
            left_index += 1
        else:
            merge_arr[temp_index] = right_arr[right_index]
            right_index += 1
        temp_index+=1

    while left_index < len(left_arr):
        merge_arr[temp_index] = left_arr[left_index]
        left_index += 1
        temp_index += 1

    while right_index < len(right_arr):
        merge_arr[temp_index] = right_arr[right_index]
        right_index += 1
        temp_index += 1

    return merge_arr


arr_in = rand.random_array([None] * 20)
print(arr_in)
arr_out = merge_sort(arr_in)

print(arr_out)
