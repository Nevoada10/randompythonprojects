# will look at the line and print line length elements.
# it will look if line length elements is equal to the height, if it is it will stop.


import sys


def main():  # Void, int
    p_height = 200
    build_pyramid(p_height)
    sn = ((p_height + 1) * p_height) / 2
    print(sn)
    return 0


def build_pyramid(p_height):
    if p_height == 0:
        return

    build_pyramid(p_height - 1)

    for _ in range(p_height):
        print(',', end='')
    print()


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)


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


def merge_sort(unordered_list):
    if len(unordered_list) <= 1:
        return unordered_list
    middle = len(unordered_list) // 2
    left_list = merge_sort(unordered_list[:middle])
    right_list = merge_sort(unordered_list[middle:])
    return merge(left_list, right_list)