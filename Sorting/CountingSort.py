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
    print("Test Input: [50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41]")
    print("Counting Sort: " + str(counting_sort([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9,41,41])))
