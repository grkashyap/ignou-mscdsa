def merge_sort(arr: list) -> list:

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    i=j=k=0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return arr

if __name__ == '__main__':
    input_arr = [23, 90, 21, 54, 76]
    print(f'unsorted list: {input_arr}')
    sorted_arr = merge_sort(input_arr)
    print(f'sorted list: {sorted_arr}')