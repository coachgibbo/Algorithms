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
	print(insertion_sort([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9]))