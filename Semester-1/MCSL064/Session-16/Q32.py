def add_sparse_matrices(m1: list, m2: list) -> list | None:

    if m1[0][0] != m2[0][0] or m1[0][1] != m2[0][1]:
        print('Addition is not possible')
        return None

    result = [[m1[0][0], m1[0][1], 0]]
    i,j = 1,1

    while i <= m1[0][2] and j <= m2[0][2]:

        if m1[i][0] < m2[j][0]:
            result.append(m1[i])
            i += 1
        elif m1[i][0] > m2[j][0]:
            result.append(m2[j])
            j += 1
        else:
            if m1[i][1] < m2[j][1]:
                result.append(m1[i])
                i += 1
            elif m1[i][1] > m2[j][1]:
                result.append(m2[j])
                j += 1
            else:
                s = m1[i][2] + m2[j][2]
                if s != 0:
                    result.append([m1[i][0], m1[i][1], s])
                i += 1
                j += 1

    while i <= m1[0][2]:
        result.append(m1[i])
        i += 1

    while j <= m2[0][2]:
        result.append(m2[j])
        j += 1

    result[0][2] = len(result) - 1

    return result

if __name__ == '__main__':

    arr1 = [
        [4, 4, 3],
        [0, 2, 5],
        [2, 0, 3],
        [3, 3, 8]
    ]

    arr2 = [
        [4, 4, 3],
        [0, 2, 2],
        [1, 1, 7],
        [3, 3, -8]
    ]

    result_arr = add_sparse_matrices(arr1, arr2)

    if result_arr is not None:
        print('Resultant Sparse Matrix: ')
        for row in result_arr:
            print(row)
    else:
        print('Addition of 2 sparse matrices is not performed')