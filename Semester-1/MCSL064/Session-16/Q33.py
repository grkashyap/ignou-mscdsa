def sparse_matrix_multiplication(m1: list, m2: list) -> list | None:
    """
        first row of the matrix is the header row and is defined as below
        [number_of rows, number_of_columns, number_of_nonzero_elements]
        all rows has [row_number, column_number, nonzero_element]
    """

    if m1[0][1] != m2[0][0]:
        print('Matrix multiplication is not possible')
        return None

    result = {}
    num_rows = m1[0][0]
    num_columns = m2[0][1]

    for idx1 in range(1, len(m1)):
        row1, col1, value1 = m1[idx1]

        for idx2 in range(1, len(m2)):
            row2, col2, value2 = m2[idx2]

            if col1 == row2:
                key = (row1, col2)
                result[key] = result.get(key,0) + value1 * value2

    sparse_result = [[num_rows, num_columns, len(result)]]
    for (r,c), v in sorted(result.items()):
        if v != 0:
            sparse_result.append([r, c, v])

    sparse_result[0][2] = len(sparse_result) - 1
    return sparse_result

if __name__ == '__main__':
    arr1 = [
        [2, 3, 3],
        [0, 0, 1],
        [0, 2, 2],
        [1, 1, 3]
    ]

    arr2 = [
        [3, 2, 3],
        [0, 1, 4],
        [1, 0, 5],
        [2, 1, 6]
    ]
    mult_result = sparse_matrix_multiplication(arr1, arr2)
    if mult_result is not None:
        for row in mult_result:
            print(row)
    else:
        print('Matrix multiplication is not performed')