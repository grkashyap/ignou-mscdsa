class QuickSort:

    def __partition(self, arr: list, low: int, high: int) -> int:
        pivot = low
        arr[pivot], arr[high] = arr[high], arr[pivot]
        for i in range(low, high):
            if arr[i] <= arr[high]:
                arr[i], arr[low] = arr[low], arr[i]
                low += 1
        arr[low], arr[high] = arr[high], arr[low]
        return low

    def quick_sort(self, arr: list, low: int, high: int) -> None:
        if low < high:
            pivot = self.__partition(arr, low, high)
            self.quick_sort(arr, low, pivot-1)
            self.quick_sort(arr, pivot+1, high)


if __name__ == '__main__':
    input_arr = [23, 90, 21, 54, 76]
    print(f'unsorted list: {input_arr}')
    quick_sort = QuickSort()
    quick_sort.quick_sort(input_arr, 0, len(input_arr)-1)
    print(f'sorted list: {input_arr}')