# -*- coding: utf-8 -*-
"""
@author: Brian Morillo

Sorting Runtime Visualizer
"""
import matplotlib.pyplot as plt
import random
from quicksort import quick_sort
from insertion_sort import insertion_sort
from timeit import default_timer as timer   

def time_algorithm(algorithm, lists_to_sort):
    """
    Measures the execution time of the given algorithm on a list.

    Parameters:
    - algorithm (callable): The sorting algorithm to be tested. 
        It should take a list as input.
    - lists (list): A list of lists to be sorted by the algorithm.

    Returns:
    list: A list containing the execution times for each input list.
    """    
    times = []

    for list in lists_to_sort:
        start = timer() 
        algorithm(list)
        times.append(timer()-start)

    return times

if __name__ == "__main__":
    n_amounts = [] # to be filled with amounts that increment by 500 up to 8000
    lists_to_sort = [] # to be filled with lists that will be used for sorting

    # Fills the amount list with values that increment
    for i in range(0, 8001, 500):
        n_amounts.append(i)

    # Fills the 'list to sort' list with lists of random values
    for n in n_amounts:
        lists_to_sort.append([random.randint(0, n) for _ in range(n)])   

    print('Generating data for insertion sort...')
    times = time_algorithm(insertion_sort, list(lists_to_sort))
    plt.plot(n_amounts, times,
              label='Insertion Sort (n^2)', color='red', marker='.', markersize='5')

    print('Generating data for quick sort...')
    times = time_algorithm(quick_sort, list(lists_to_sort))    
    plt.plot(n_amounts, times,
              label='Quick Sort (nlogn)', color='green', marker='.', markersize='5')
    
    # Displays runtime data on a graph
    print('Displaying data...')
    plt.title('Sorting Algorithms Runtimes')
    plt.xlabel('Number of elements')
    plt.ylabel('time(seconds)')
    plt.legend()
    plt.show()