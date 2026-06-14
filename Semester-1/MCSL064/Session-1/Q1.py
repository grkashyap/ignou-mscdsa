def count_words(input_str: str) -> int:
    words = input_str.split(' ')
    return len(words)

def count_whitespaces(input_str: str) -> int:
    whitespaces = 0
    for word in input_str:
        if word.isspace():
            whitespaces += 1
    return whitespaces

def count_characters(input_str: str) -> int:
    characters = 0
    for char in input_str:
        characters += 1
    return characters

if __name__ == '__main__':
    input_str = input("Enter a string: ")
    num_words = count_words(input_str)
    print(f'There are {num_words} words in {input_str}.')
    
    num_whitespaces = count_whitespaces(input_str)
    print(f'There are {num_whitespaces} whitespaces in {input_str}.')

    num_characters = count_characters(input_str)
    print(f'There are {num_characters} characters in {input_str}.')
