import TestData
import random
import Sorting.QuickSort as Partitioning


def quick_select_naive(array, k):
    n = len(array)
    if n > 1:
        pivot = random.randint(0, n-1)
        partitioned_array, mid = Partitioning.naive_partition(array, pivot)
        if k-1 < mid:
            return quick_select_naive(partitioned_array, k)
        elif k-1 > mid:
            return quick_select_naive(partitioned_array, k)
        else:
            return partitioned_array[mid]
    else:
        return array[0]


def quick_select_hoares(array, k):
    n = len(array)
    if n > 1:
        pivot = random.randint(0, n-1)
        partitioned_array, mid = Partitioning.hoares_partition(array, pivot)
        if k-1 < mid:
            return quick_select_hoares(partitioned_array, k)
        elif k-1 > mid:
            return quick_select_hoares(partitioned_array, k)
        else:
            return partitioned_array[mid]
    else:
        return array[0]


if __name__ == "__main__":
    test_input = TestData.generate_list_of_ints(1, 200, 20)
    print("Test Input: " + str(test_input))
    print("Sorted Test Input: " + str(sorted(test_input)))
    print("Naive QuickSelect k=3: " + str(quick_select_naive(test_input, 3)))
    print("Naive QuickSelect k=7: " + str(quick_select_naive(test_input, 7)))
    print("Naive QuickSelect k=12: " + str(quick_select_naive(test_input, 12)))
    print("Naive QuickSelect k=20: " + str(quick_select_naive(test_input, 20)))
    print("Hoare's QuickSelect k=3: " + str(quick_select_hoares(test_input, 3)))
    print("Hoare's QuickSelect k=7: " + str(quick_select_hoares(test_input, 7)))
    print("Hoare's QuickSelect k=12: " + str(quick_select_hoares(test_input, 12)))
    print("Hoare's QuickSelect k=20: " + str(quick_select_hoares(test_input, 20)))
