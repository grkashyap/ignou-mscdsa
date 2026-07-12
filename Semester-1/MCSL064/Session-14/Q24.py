def insertion_sort(arr:list) -> list:
    arr_len = len(arr)
    for i in range(arr_len):
        temp = arr[i]
        j = i
        while j > 0 and arr[j-1] > temp:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = temp
    return arr

if __name__ == '__main__':
    unsorted_arr = [23, 90, 21, 54, 76]
    print(f'Unsorted array: {unsorted_arr}')
    sorted_arr = insertion_sort(unsorted_arr)
    print(f'Sorted array: {sorted_arr}')