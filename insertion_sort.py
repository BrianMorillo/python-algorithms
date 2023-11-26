# -*- coding: utf-8 -*-
"""
@author: Brian Morillo

Insertion Sort 
Time Complexity: O(n^2)
"""
    
def insertion_sort(arr):
    n = len(arr) # gets the n length of the array

    # Checks if the array is empty or only has one value
    if n <= 1:
        return

    for i in range(1, n):
        # Stores current value as the key to insert
        key = arr[i] 

        j = i - 1

        # Shifts elements that are bigger than the key to the right
        while j >= 0 and arr[j] > key:
            swap(arr, j + 1, j)
            j = j - 1

        arr[j + 1] = key # Inserts key

            
def swap(values, i1, i2):
    """
    Swaps two values in a list.    

    Parameters
    ----------
    values : list
        list where the values will be swapped.
    i1 : int
        Index of the first value.
    i2 : int
        Index of the second value.

    """
    values[i1], values[i2] = values[i2], values[i1]
    