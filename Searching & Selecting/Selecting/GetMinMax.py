import TestData


def getMin(array):
    minimum = array[0]
    for integer in array:
        if integer < minimum:
            minimum = integer
    return minimum


def getMax(array):
    maximum = array[0]
    for integer in array:
        if integer > maximum:
            maximum = integer
    return maximum


def getOptimizedMinMax(array):
    n = len(array)
    if n % 2 != 0:
        minimum, maximum, start_index = array[1], array[1], 1
    else:
        if array[0] < array[1]:
            minimum, maximum, start_index = array[0], array[1], 2
        else:
            minimum, maximum, start_index = array[1], array[0], 2

    for i in range(start_index, n, 2):
        if array[i] < array[i+1]:
            if array[i] < minimum:
                minimum = array[i]
            if array[i+1] > maximum:
                maximum = array[i+1]
        else:
            if array[i] > maximum:
                maximum = array[i]
            if array[i+1] < minimum:
                minimum = array[i+1]

    return minimum, maximum


if __name__ == "__main__":
    test_input = TestData.generate_list_of_ints(1, 200, 20)
    print("Test Input: " + str(test_input))
    print("Min: " + str(getMin(test_input)))
    print("Max: " + str(getMax(test_input)))
    optMinMax = getOptimizedMinMax(test_input)
    print(str.format("Optimized Min: {} and Optimized Max: {}", optMinMax[0], optMinMax[1]))
