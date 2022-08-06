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
    print(binary_search([5, 9, 17, 21, 28, 31, 41, 43, 44, 45, 50, 55, 61, 68, 69, 71, 72, 73, 75, 78, 88, 93, 97, 99], 99))
