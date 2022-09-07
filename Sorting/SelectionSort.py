import TestData


def selection_sort(array):
	n = len(array)
	
	for i in range(0, n):
		min = array[i]
		min_ind = i
		for j in range(i, n):
			if array[j] < min:
				min = array[j]
				min_ind = j
		array[min_ind] = array[i]
		array[i] = min
	
	return array


if __name__ == '__main__':
	test_input = TestData.generate_list_of_ints(1, 50000, 500)
	print("Test Input: " + str(test_input))
	print("Selection Sort: " + str(selection_sort(test_input)))
