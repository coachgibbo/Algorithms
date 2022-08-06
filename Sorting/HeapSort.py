import BinaryHeap


def heap_sort(array):
	n = len(array)
	heap = BinaryHeap.BinaryHeap(array)

	for i in range(0, n):
		heap.delete()
	
	return array


if __name__ == "__main__":
	print(heap_sort([50,31,21,28,72,41,73,93,68,43,45,78,5,17,97,71,69,61,88,75,99,44,55,9]))
		