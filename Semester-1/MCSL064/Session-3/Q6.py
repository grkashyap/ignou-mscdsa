def factorial(n: int) -> int:

    if n <= 1: return 1

    return n * factorial(n-1)

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    if num <= 0:
        print('Enter a positive integer')
    num_factorial = factorial(num)
    print(f'Factorial of {num} is {num_factorial}')