def factorial(n: int) -> int:

    if n == 0: return 1

    if n == 1: return 1

    return n * factorial(n-1)

if __name__ == '__main__':
    num = int(input('Enter a number: '))
    num_factorial = factorial(num)
    print(f'Factorial of {num} is {num_factorial}')