# Search Algorithms:
# 	Linear Search
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i


# 	Binary Search
def binary_search(list, target):
    first = 0
    last = len(list) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            found = True
        else:
            if target < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


# 	Hash Table


# Sorting Algorithms:
# 	Bubble Sort
def bubble_sort(list):
    for i in range(len(list) - 1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    return list


# 	Selection Sort ( Selection by the smallest number, or biggest number )
def selection_sort(list):
    for i in range(0, len(list) - 1):
        min = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min]:
                min = j
        temp = list[i]
        list[i] = list[min]
        list[min] = temp
    return list


# Merge Sort ( Recursive sorting )
def merge_sort(list):
    if len(list) > 1:
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list[k] = left[i]
                i += 1
            else:
                list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            list[k] = left[i]
            i += 1
            k += 1
