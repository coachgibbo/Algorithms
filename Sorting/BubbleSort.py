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
    print(bubble_sort([50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78, 5, 17, 97, 71, 69, 61, 88, 75, 99, 44, 55, 9]))