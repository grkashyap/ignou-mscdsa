def reverse_string_slicing(input_str: str) -> str:
    return input_str[::-1]

def reverse_string_functions(input_str: str) -> str:
    result = ''

    for i in range(len(input_str)-1,-1,-1):
        result += input_str[i]

    return result

if __name__ == '__main__':
    input_str = input('Enter a string: ')
    reversed_str = reverse_string_slicing(input_str)
    print(f'Reversed string using slicing: {reversed_str}')

    reversed_str_using_function = reverse_string_functions(input_str)
    print(f'Reversed string using functions: {reversed_str_using_function}')