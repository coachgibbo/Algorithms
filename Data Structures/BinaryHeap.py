class BinaryHeap:
    # The heap is represented as an array
    # The child of node i is located at 2*i and (2*i)+1
    def __init__(self, array) -> None:
        self.array = array
        self.length = len(array)

        self.heapify()

    # We start at the middle node, and iterate backwards to the root node
    # We 'fall' each node, meaning we drop it down the tree into position
    # This naturally ensures that the highest nodes get filtered up to the top
    def heapify(self) -> None:
        for i in range(self.length // 2, -1, -1):
            self.fall(i)

    # We append the new value as the last node in the heap
    # We then 'rise' the node, comparing it with it's parent until it's in position
    def insert(self, value) -> None:
        self.array.append(value)
        self.length += 1
        self.rise(self.length - 1)

    # We swap the root node with the last node in the heap
    # We don't pop the element, instead we leave it in position n and decrement self.length
    # This allows us to use heap sort if required
    # We 'fall' the node from the root back into its position
    def delete(self) -> None:
        self.array[0], self.array[self.length - 1] = self.array[self.length - 1], self.array[0]
        output = self.array[self.length - 1]
        self.length -= 1
        self.fall(0)

        return output

    # A method to raise a node i into position by comparing it with its parent
    # Gets the parent and starts a while loop
    # 		The loop breaks if parent=0 (meaning it's at the root) or if the child's position is good
    def rise(self, i):
        parent = (i - 1) // 2

        while parent >= 0:
            if self.array[parent] < self.array[i]:
                self.array[i], self.array[parent] = self.array[parent], self.array[i]
                i = parent
                parent = i // 2
            else:
                break

    # A method to drop a node i into position by comparing with its children
    # Sets the child and starts a while loop
    # 		The loop breaks if child<=length (meaning it's at lowest level)
    # 		Or if i's position is fine (not smaller than children)
    # The first if statement in the loop checks if there are two children and if child+1 is greater than child
    # This sets which child is good to use for swapping elements if required
    # To switch from a max heap to a min heap, swap the operators on the array element comparisons
    # (line 28 #2 and line 31)
    def fall(self, i):
        child = 2 * (i + 1)

        while child <= self.length:
            if child < self.length and self.array[child] > self.array[child - 1]:
                child += 1

            if self.array[i] < self.array[child - 1]:
                self.array[i], self.array[child - 1] = self.array[child - 1], self.array[i]
                i = child - 1
                child = 2 * (i + 1)
            else:
                break


if __name__ == '__main__':
    input1 = [50, 31, 21, 28, 72]
    # heap1 = BinaryHeap(input1)

    input2 = [50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78, 5]
    # heap2 = BinaryHeap(input2)

    input3 = [50, 31, 21, 28, 72, 41, 73, 93, 68, 43, 45, 78, 5, 17, 97, 71, 69, 61, 88, 75, 99, 44, 55, 9]
    # heap3 = BinaryHeap(input3)
    # print(heap3.array)
