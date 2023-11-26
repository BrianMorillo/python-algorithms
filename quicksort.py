# -*- coding: utf-8 -*-
"""
@author: Brian Morillo

Randomized Quick Sort approach
Time Complexity: O(nlogn)
"""
import random
    
def quick_sort(values, l=0, r=None):
    """
    Sorts a list using the randomized quick sort approach

    Parameters
    ----------
    values : list
        List of values to sort.
    l : int, optional
        The left most index of the sublist to be sorted. The default is 0.
    r : int, optional
        The right most index of the sublist to be sorted.. The default is None.
    """
    if r is None:
        r = len(values)
        
    # Only partition if the amount of values to sort is bigger than 1
    if l < r:
        i = rand_partition(values, l, r)
        quick_sort(values, l, i)
        quick_sort(values, i + 1, r)
        
def partition(values, l, r):
    """
    Partitions a sublist for the Quick Sort algorithm.
    
    Parameters
    ----------
    values : list
        The list of values to be partitioned..
    l : int
        The left most index of the sublist to be partitioned.
    r : int
        The right most index of the sublist to be partitioned.

    Returns
    -------
    i : int
        The pivot index after partitioning.

    """
    pivot = values[l]
    i = l
    
    for j in range(l + 1, r):
        # only swap values smaller than the pivot towards the left
        if values[j] <= pivot:
            i = i + 1
            swap(values, i, j)
            
    swap(values, i, l)
    return i

def rand_partition(values, l, r):
    """
    Chooses a random pivot for partitioning.

    Parameters
    ----------
    values : list
        The list of values to choose a pivot from.
    l : int
        The left most index of the sublist.
    r : int
        The right most index of the sublist..

    Returns
    -------
    int
        The pivot index after partitioning.

    """
	# 0 is inclusive, r - l is inclusive
    i = random.randint(0, r - l - 1) + l
    swap(values, r - 1, i)
    return partition(values, l, r);
            
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
            
            
    