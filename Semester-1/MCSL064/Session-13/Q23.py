def selection_sort(arr: list) -> list:
    arr_len = len(arr)
    for i in range(arr_len):
        min_idx = i
        for j in range(i + 1, arr_len):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[min_idx], arr[i] = arr[i], arr[min_idx]
    return arr

if __name__ == '__main__':
    unsorted_list = [23, 90, 21, 54, 76]
    print(f'Unsorted list: {unsorted_list}')
    sorted_list = selection_sort(unsorted_list)
    print(f'Sorted list: {sorted_list}')
