# -*- coding: utf-8 -*-
"""
@author: Brian Morillo

Randomized Quick Sort test
"""
import pytest
from insertion_sort import insertion_sort
from quicksort import quick_sort
algorithm_list = [insertion_sort, quick_sort]

# Test case 1: Sort an empty list
@pytest.mark.parametrize("sorting_algorithm", algorithm_list)
def test_empty_list(sorting_algorithm):
    input_list = []
    expected_output = []
    sorting_algorithm(input_list)
    assert input_list == expected_output

# Test case 2: Sort a list with one element
@pytest.mark.parametrize("sorting_algorithm", algorithm_list)
def test_single_element_list(sorting_algorithm):
    input_list = [42]
    expected_output = [42]
    sorting_algorithm(input_list)
    assert input_list == expected_output

# Test case 3: Sort a list with multiple elements
@pytest.mark.parametrize("sorting_algorithm", algorithm_list)
def test_multi_element_list(sorting_algorithm):
    input_list = [9, 7, 5, 11, 12, 2, 14]
    expected_output = [2, 5, 7, 9, 11, 12, 14]
    sorting_algorithm(input_list)
    assert input_list == expected_output
    
# Test case 4: Sort a list with some duplicate elements
@pytest.mark.parametrize("sorting_algorithm", algorithm_list)
def test_duplicate_element_list(sorting_algorithm):
    input_list = [9, 9, 9, 11, 2, 2, 14]
    expected_output = [2, 2, 9, 9, 9, 11, 14]
    sorting_algorithm(input_list)
    assert input_list == expected_output    

if __name__ == '__main__':
    pytest.main()