def quick_sort_naive(array):
    n = len(array)

    if n > 1:
        partitioned, pivot = naive_partition(array, 1)
        left = quick_sort_naive(partitioned[0:pivot])
        right = quick_sort_naive(partitioned[pivot+1:n])
        return left + [partitioned[pivot]] + right

    return array


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
    return array, len(left) + len(pivots)//2


def quick_sort_hoares(array):
    n = len(array)

    if n > 1:
        pivots = hoares_partition(array, 1)
        left = quick_sort_hoares(array[0:pivots])
        right = quick_sort_hoares(array[pivots+1:n])
        return left + [array[pivots]] + right

    return array


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
    return j


def quick_sort_dnf(array):
    n = len(array)

    if n > 1:
        pivots = dnf_partition(array, array[1])
        left = quick_sort_dnf(array[0:pivots[0]])
        right = quick_sort_dnf(array[pivots[1]:n])
        return left + array[pivots[0]:pivots[1]] + right

    return array


# Dutch National Flag Partitioning
def dnf_partition(array, pivot):
    boundary1 = 0
    j = 0
    boundary2 = len(array) - 1

    while j <= boundary2:
        if array[j] < pivot:
            array[j], array[boundary1] = array[boundary1], array[j]
            boundary1 += 1
            j += 1
        elif array[j] == pivot:
            j += 1
        else:
            array[j], array[boundary2] = array[boundary2], array[j]
            boundary2 -= 1

    return boundary1, j-1


if __name__ == "__main__":
    print("Test Input: [50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41]")
    print("Quick Sort (Naive): " + str(quick_sort_naive([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41])))
    print("Quick Sort (Hoare's): " + str(quick_sort_hoares([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41])))
    print("Quick Sort (DNF): " + str(quick_sort_dnf([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41])))
