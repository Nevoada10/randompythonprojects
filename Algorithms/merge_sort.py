# Merge Sort Algorithm

import random




def main():
    # Create random list
    r_list = random.sample(range(1, 1000), 500)
    print("Random list:", r_list)

    # Sort list
    o_list = merge_sort(r_list)
    print("Sorted list:", o_list)


def merge_sort(unordered_list):
    def merge(left_list, right_list):
        merged_list = []
        left_list_index = right_list_index = 0
        while left_list_index < len(left_list) and right_list_index < len(right_list):
                if left_list[left_list_index] < right_list[right_list_index]:
                merged_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                merged_list.append(right_list[right_list_index])
                right_list_index += 1
        merged_list += left_list[left_list_index:]
        merged_list += right_list[right_list_index:]
        return merged_list

    if len(unordered_list) <= 1:
        return unordered_list
    middle = len(unordered_list) // 2
    left_list = merge_sort(unordered_list[:middle])
    right_list = merge_sort(unordered_list[middle:])
    return merge(left_list, right_list)

main()