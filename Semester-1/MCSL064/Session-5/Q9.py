def num_product(num1: int, num2: int) -> int:

    if num2 == 0:
        return 0

    return num1 + num_product(num1, num2-1)

if __name__=='__main__':
    n1 = int(input('Enter first number: '))
    n2 = int(input('Enter second number: '))
    result = num_product(n1, n2)
    print(f'Product of {n1} and {n2} is {result}')