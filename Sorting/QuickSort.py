def naive_partition(array, pivot_index):
    left = []
    pivots = []
    right = []
    pivot = array[pivot_index]

    for i in array:
        if i < pivot:
            left.append(i)
        elif i == pivot:
            pivots.append(i)
        else:
            right.append(i)

    array = left + pivots + right
    print(array)
    return len(left) + len(pivots)//2


def hoares_partition(array, pivot_index):
    array[0], array[pivot_index] = array[pivot_index], array[0]
    i = 1
    j = len(array) - 1

    while i <= j:
        while i <= j and array[i] <= array[0]:
            i += 1
        while i <= j and array[j] > array[0]:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]

    array[0], array[j] = array[j], array[0]
    print(array)
    return j


# Dutch National Flag Partitioning
def dnf_partition(array, pivot_index):
    boundary1 = j = 0
    boundary2 = len(array) - 1
    while j <= boundary2:
        if array[j] < array[pivot_index]:
            array[j], array[boundary1] = array[boundary1], array[j]
            boundary1 += 1
            j += 1
        elif array[j] == array[pivot_index]:
            j += 1
        else:
            array[j], array[boundary2] = array[boundary2], array[j]
            boundary2 -= 1

    print(array)
    return boundary1, j-1


if __name__ == "__main__":
    print("Naive Partition Result: " + str(naive_partition([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9], 5)))
    print("Hoare's Partition Result: " + str(hoares_partition([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9], 5)))
    print("Dutch National Flag Partition Result: " + str(dnf_partition([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9, 41, 41], 5)))
