import TestData


def binary_search(array, target):
    lo = 0
    hi = len(array) - 1
    mid = 0

    while lo <= hi:
        mid = (lo + hi) // 2
        if target > array[mid]:
            lo = mid + 1
        elif target < array[mid]:
            hi = mid - 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    test_input = TestData.generate_sorted_list_of_ints_with_target(1, 200, 20, 49)
    print("Test Input: " + str(test_input))
    print("Binary Search - 49 is at index " + str(binary_search(test_input, 49)))
