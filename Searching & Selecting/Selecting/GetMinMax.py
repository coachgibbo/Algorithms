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


if __name__ == "__main__":
    test_input = TestData.generate_list_of_ints(1, 200, 20)
    print("Test Input: " + str(test_input))
    print("Min: " + str(getMin(test_input)))
    print("Max: " + str(getMax(test_input)))
