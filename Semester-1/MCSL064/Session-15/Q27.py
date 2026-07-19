class HeapSort:

    def heap_sort(self, arr:list) -> None:
        arr_len = len(arr)
        for i in range(arr_len//2-1, -1, -1):
            self.__heapify(arr, arr_len, i)

        for i in range(arr_len-1, 0, -1):
            arr[0], arr[i] = arr[i], arr[0]
            self.__heapify(arr, i, 0)

    def __heapify(self, arr:list, arr_len: int, curr_idx:int) -> None:

        largest_idx = curr_idx
        left_child = curr_idx * 2 + 1
        right_child = curr_idx * 2 + 2

        if left_child < arr_len and arr[left_child] > arr[largest_idx]:
            largest_idx = left_child

        if right_child < arr_len and arr[right_child] > arr[largest_idx]:
            largest_idx = right_child

        if largest_idx != curr_idx:
            arr[curr_idx], arr[largest_idx] = arr[largest_idx], arr[curr_idx]
            self.__heapify(arr, arr_len, largest_idx)

if __name__ == '__main__':
    input_arr = [9, 4, 3, 8, 10, 2, 5]
    heap_sort = HeapSort()
    heap_sort.heap_sort(input_arr)
    for num in range(len(input_arr)):
        print(input_arr[num], end=' ')
