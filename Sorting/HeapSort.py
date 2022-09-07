from DataStructures import BinaryHeap

import TestData


def heap_sort(array):
	n = len(array)
	heap = BinaryHeap.BinaryHeap(array)

	for i in range(0, n):
		heap.delete()
	
	return array


if __name__ == "__main__":
	test_input = TestData.generate_list_of_ints(1, 50000, 500)
	print("Test Input: " + str(test_input))
	print("Heap Sort: " + str(heap_sort(test_input)))
		