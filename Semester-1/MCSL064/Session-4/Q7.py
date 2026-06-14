def fibbanoci_series_recursion(num: int) -> int:
    if num == 0:
        return 0

    if num == 1:
        return 1

    return fibbanoci_series_recursion(num-1)+fibbanoci_series_recursion(num-2)

def fibanoci_series_iterative(num: int) -> int:
    n1, n2 = 0, 1
    for i in range(num):
        print(n1, end=' ')
        n1, n2 = n2, n1 + n2


if __name__ == '__main__':
    input_num = int(input('Enter a number: '))
    print('Fibanoci Series using recursion')
    for i in range(input_num):
        print(fibbanoci_series_recursion(i), end=' ')
    print('\nFibanoci Series using iterative')
    fibanoci_series_iterative(input_num)