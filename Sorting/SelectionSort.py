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
	selection_sort([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9])