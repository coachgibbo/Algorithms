import TestData


def insertion_sort(array):
	n = len(array)

	for i in range(1, n):
		curr = array[i]
		j = i - 1
		while j >= 0 and array[j] > curr:
			array[j+1] = array[j]
			j -= 1
		array[j+1] = curr

	return array


if __name__ == '__main__':
	test_input = TestData.generate_list_of_ints(1, 50000, 500)
	print("Test Input: " + str(test_input))
	print("Insertion Sort: " + str(insertion_sort(test_input)))

