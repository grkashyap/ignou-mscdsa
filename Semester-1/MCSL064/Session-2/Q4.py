def change_letter_case(input_str: str) -> str:
    result = ''

    for ch in input_str:
        if ch.isupper():
            result += ch.lower()
        elif ch.islower():
            result += ch.upper()
        else:
            result += ch

    return result

if __name__ == '__main__':
    input_str = input('Enter a string: ')
    result = change_letter_case(input_str)
    print(f'Result is {result}')