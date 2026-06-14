def reverse_string(input_str: str, index:int) -> str:

    if len(input_str) == 0:
        return ''

    if index == 0:
        return input_str[index]

    return input_str[index]+reverse_string(input_str, index-1)


if __name__ == '__main__':
    s = input('Enter a string: ')
    result = reverse_string(s, len(s)-1)
    print(f'The reverse of {s} is {result}')