import TestData


def counting_sort(array):
    u = max(array) + 1
    n = len(array)
    counter = [0] * u
    for num in array:
        counter[num] += 1

    position = [0] * u
    position[0] = 1
    for i in range(1, u-1):
        position[i] = position[i-1] + counter[i-1]

    temp = [0] * n
    for j in range(0, n):
        temp[position[array[j]] - 1] = array[j]
        position[array[j]] -= 1

    return temp


if __name__ == "__main__":
    test_input = TestData.generate_list_of_ints(1, 50000, 500)
    print("Test Input: " + str(test_input))
    print("Counting Sort: " + str(counting_sort(test_input)))
