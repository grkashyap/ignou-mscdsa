def count_frequency(input_str: str, freq_dict: dict, index: int = 0) -> dict:

    if index == len(input_str):
        return freq_dict

    word = input_str[index]

    if word == ' ':
        return count_frequency(input_str, freq_dict, index+1)

    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

    return count_frequency(input_str, freq_dict, index+1)


if __name__=='__main__':
    input_str = input('Enter a string: ')
    freq_dict = count_frequency(input_str, {})
    print(freq_dict)