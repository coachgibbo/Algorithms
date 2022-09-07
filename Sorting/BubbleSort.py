import TestData


def bubble_sort(array):
    n = len(array)

    for i in range(0, n-1):
        swapped = False

        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True

        if not swapped:
            return array

    return array


if __name__ == '__main__':
    test_input = TestData.generate_list_of_ints(1, 50000, 500)
    print("Test Input: " + str(test_input))
    print("Bubble Sort: " + str(bubble_sort(test_input)))
