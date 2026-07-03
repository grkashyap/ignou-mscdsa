def generate_subsets(input_set: list, subsets: list[set], index: int = 0) -> list:

    if index == len(input_set):
        return [set()]

    value = input_set[index]

    subsets.append(set(value))

    remaining_subsets = generate_subsets(input_set, subsets, index + 1)

    subsets = [subset.union({value}) for subset in remaining_subsets]

    return subsets + remaining_subsets

if __name__ == '__main__':
    str_lst = input('Enter values of set separated by space in a single line: ')
    str_lst_arr = str_lst.split(' ')
    input_set = []
    for item in str_lst_arr:
        input_set.append(item)

    subset_lst = generate_subsets(input_set, [])
    print(subset_lst)