import TestData


def merge_sort(array):
    n = len(array)

    if n > 1:
        mid = n // 2
        merged_array1 = merge_sort(array[:mid])
        merged_array2 = merge_sort(array[mid:])
        array = merge(merged_array1, merged_array2)

    return array


def merge(array1, array2):
    result = []
    n1 = len(array1)
    n2 = len(array2)

    # Create two pointers, i for array1 and j for array2
    # Increment until n1 or n2 is reached, meaning the end of one of the arrays
    i = j = 0
    while i < n1 and j < n2:
        if i < n1 and array1[i] <= array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    # Put the leftover elements from array1 or array2 into the result array
    while i != n1:
        result.append(array1[i])
        i += 1

    while j != n2:
        result.append(array2[j])
        j += 1

    return result


if __name__ == "__main__":
    test_input = TestData.generate_list_of_ints(1, 50000, 500)
    print("Test Input: " + str(test_input))
    print("Merge Sort: " + str(merge_sort(test_input)))
