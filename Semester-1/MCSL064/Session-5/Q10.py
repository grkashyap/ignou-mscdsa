def generate_subsets(input_set: list, subsets: list[set], index: int = 0) -> list:

    if index == len(input_set):
        return [set()]

    value = input_set[index]
    subsets.append(set(value))
    remaining_subsets = generate_subsets(input_set, subsets, index + 1)
    subsets = [subset.union({value}) for subset in remaining_subsets]
    return subsets + remaining_subsets

if __name__ == '__main__':
    str_lst = input('Enter values of set separated by comma in a single line: ')
    input_set = str_lst.split(',')
    subset_lst = generate_subsets(input_set, [])
    print(subset_lst)