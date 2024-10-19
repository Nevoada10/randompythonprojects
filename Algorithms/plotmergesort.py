#######################################################################################################################
# Nevoada
#######################################################################################################################

# Title: Merge Sort
# Author: Nevoada
# Year: 2023
# Description: A simple visual representation in Python for merge sort algorithm.

# ===================================================================================================================
# PSEUDOCODE:
# ===================================================================================================================

# 1. Divide the list into two halves
# 2. Sort each half
# 3. Merge the sorted halves
# 4. Repeat steps 1-3 until the list is sorted


# =================================================================================================================
# IMPORTS:
# =================================================================================================================

import sys
import random
import matplotlib.pyplot as plt
import numpy as np


# =================================================================================================================
# FUNCTIONS:
# =================================================================================================================
def merge_sort_only(unordered_list):
    def merge(left_list, right_list):  # Merge two lists
        merged_list = []
        left_list_index = right_list_index = 0
        while left_list_index < len(left_list) and right_list_index < len(right_list):  # While both lists have values.
            if left_list[left_list_index] < right_list[right_list_index]:  # If the left value is smaller, append it.
                merged_list.append(left_list[left_list_index])  # Append the smaller value on the left list.
                left_list_index += 1  # Go to the next value in the left list. [ {1}, (2) ,3 ]
            else:  # If the right value is smaller, append it to the merged list (final list).
                merged_list.append(right_list[right_list_index])  # Append the smaller value on the right list.
                right_list_index += 1  # Go to the next value in the right list. R [ [1], (2) ,3 ]
        merged_list += left_list[left_list_index:]  # Add the rest of the left list to the merged list.
        merged_list += right_list[right_list_index:]    # Add the rest of the right list to the merged list.
        return merged_list  # Return the merged list, the sorted list.

    # Base case, n = 1
    if len(unordered_list) <= 1:  # If the list has only one value
        return unordered_list  # Return the list

    # Recursive case
    middle = len(unordered_list) // 2  # Define the where is middle of the list
    left_list = merge_sort_only(unordered_list[:middle])  # Split the list in two and recall the function.
    right_list = merge_sort_only(unordered_list[middle:])  # Right part by the middle.

    sorted_list = merge(left_list, right_list)  # Sort and merge the two lists into one.

    return sorted_list


def merge_sort(unordered_list, animate=False, ax=None):
    def merge(left_list, right_list):  # Merge two lists
        merged_list = []    # Initialize the merged list for appending values.
        left_list_index = right_list_index = 0  # Initialize the index of the left and right list.
        while left_list_index < len(left_list) and right_list_index < len(right_list):  # While both lists have values.
            if left_list[left_list_index] < right_list[right_list_index]:  # If the L list value is smaller, append it.
                merged_list.append(left_list[left_list_index])  # Append the smaller value on the left list.
                left_list_index += 1  # Go to the next value in the left list. [ {1}, (2) ,3 ]
            else:  # If the right R value is smaller, append it to the merged list (final list).
                merged_list.append(right_list[right_list_index])  # Append the smaller value on the right list.
                right_list_index += 1  # Go to the next value in the right list. [ 1, {2} ,3 ]
        merged_list += left_list[left_list_index:]  # Add the rest of the left list to the merged list.
        merged_list += right_list[right_list_index:]    # Add the rest of the right list to the merged list.
        return merged_list  # Return the merged list, the sorted list.

    # Base case, n = 1
    if len(unordered_list) <= 1:  # If the list has only one value
        return unordered_list  # Return the list

    # Recursive case
    middle = len(unordered_list) // 2  # Define the where is middle of the list
    left_list = merge_sort(unordered_list[:middle], animate, ax)  # Split the list in tw and recall the function.
    right_list = merge_sort(unordered_list[middle:], animate, ax)  # Right part by the middle.

    sorted_list = merge(left_list, right_list)  # Sort and merge the two lists into one.

    if animate:
        ax.clear()
        ax.bar(np.arange(len(sorted_list)), sorted_list)
        ax.set_title('Sorting Process')
        plt.pause(0.001)

    return sorted_list


# ===================================================================================================================
# MAIN:
# ===================================================================================================================

def main():
    # Create random list
    r_list = random.sample(range(1, 1000), 500)
    print("Random list:", r_list)

    # Plot random list ( 1st subplot)
    fig, axs = plt.subplots(1, 3, figsize=(10, 5))  # Create Subplots. 1 row, 2 columns
    bar1 = axs[0].bar(np.arange(len(r_list)), r_list)  # Bar plot
    axs[0].set_title('Unordered List')

    # Sort list only, no animation. (3rd subplot)
    o_list = merge_sort_only(r_list)
    print("Sorted list:", o_list)
    # Plot sorted list ( 3rd subplot)
    bar2 = axs[2].bar(np.arange(len(o_list)), o_list)  # Bar plot
    axs[2].set_title('Sorted List')

    # Animation (2nd subplot)
    # Define subplot name as "Sorting Process"
    sorted_list = merge_sort(r_list, animate=True, ax=axs[1])
    axs[1].set_title('Sorting Process')

    plt.show()

    return 0    # Convention for successful execution.


if __name__ == "__main__":  # Check if it's main otherwise it won't run
    exit_code = main()  # Call the main function
    sys.exit(exit_code)  # Exit the program
