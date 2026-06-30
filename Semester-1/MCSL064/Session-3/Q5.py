def count_frequency(words: list, freq_dict: dict, index: int = 0) -> dict:

    if index == len(words):
        return freq_dict

    word = words[index]

    if word == ' ':
        return count_frequency(words, freq_dict, index + 1)

    if word in freq_dict:
        freq_dict[word] += 1
    else:
        freq_dict[word] = 1

    return count_frequency(words, freq_dict, index + 1)


if __name__=='__main__':
    input_str = input('Enter a string: ')
    words = input_str.split()
    freq_dict = count_frequency(words, {})
    print(freq_dict)