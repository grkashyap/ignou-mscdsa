def binary_search_iter(arr: list, key: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if key < arr[mid]:
            high = mid - 1
        elif key > arr[mid]:
            low = mid + 1
        elif key == arr[mid]:
            return mid

    return -1

def binary_search(arr: list, low: int, high: int, key: int) -> int:
    if low > high:
        return -1
    mid = (low + high) // 2
    if key < arr[mid]:
        return binary_search(arr, low, mid - 1, key)
    elif key > arr[mid]:
        return binary_search(arr, mid + 1, high, key)
    else:
        return mid


if __name__ == '__main__':
    input_arr = [21, 23, 54, 76, 90]
    search_key = 54
    idx = binary_search_iter(input_arr, search_key)
    if idx == -1:
        print('Value not found')
    else:
        print(f'{input_arr[idx]} found at index {idx}')

    idx_recursive = binary_search(input_arr, 0, len(input_arr) - 1, search_key)
    if idx_recursive == -1:
        print('Value not found')
    else:
        print(f'{input_arr[idx_recursive]} found at index {idx_recursive}')