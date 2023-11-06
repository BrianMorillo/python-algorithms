# -*- coding: utf-8 -*-
"""
@author: Brian Morillo

Visualization of Randomized Quick Sort
"""

import matplotlib.pyplot as plt
import numpy as np
import quicksort
    
def swap_visualize(values, i1, i2):
    """
    Swaps two values in a list and updates graph visualization

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
    updates_graph()

def updates_graph():
    """
    Updates the graph visualization
    """   
    plt.title("Quicksort")
    plt.xlabel("Index")
    plt.ylabel("Value")       
    plt.bar(x, list, color='red')
    plt.pause(0.001)
    plt.clf()

amount = 50
list = np.random.randint(0, 100, amount)
x = np.arange(0, amount, 1)
            
if __name__ == "__main__":
    # Overrides the default swap function in order to see the graph updates
    quicksort.swap = swap_visualize

    # starts quick sort 
    quicksort.quick_sort(list)

    # Final visualization of the sorted data
    plt.bar(x, list)
    plt.show()  # Shows the Matplotlib plots  