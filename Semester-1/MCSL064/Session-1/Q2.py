def replace_multiple_whitespaces(input_str: str) -> str:

    str_len = len(input_str)
    new_str = ""
    prev_space = False

    for i in range(str_len):
        if input_str[i] == " ":
            if not prev_space:
                new_str += input_str[i]
                prev_space = True
        else:
            new_str += input_str[i]
            prev_space = False

    return new_str

if __name__ == "__main__":
    input_str = input("Enter a string: ")
    updated_str = replace_multiple_whitespaces(input_str)
    print(f'Original String: {input_str}')
    print(f'Updated String: {updated_str}')