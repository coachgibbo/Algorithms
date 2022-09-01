def radix_sort(array, base):
    max_element = max(array)
    digit = 1
    while max_element // digit > 0:
        array = radix_pass(array, digit, base)
        digit *= base

    return array


def radix_pass(array, digit, base):
    n = len(array)
    count = [0] * base
    for num in array:
        count[(num // digit) % base] += 1

    position = [0] * base
    position[0] = 1
    for i in range(1, base):
        position[i] = position[i-1] + count[i-1]

    temp = [0] * n
    for j in range(0, n):
        index = array[j] // digit
        temp[position[index % base] - 1] = array[j]
        position[index % base] += 1

    return temp


if __name__ == "__main__":
    print("Test Input: [50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41]")
    print("Radix Sort: " + str(radix_sort([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41], 2)))