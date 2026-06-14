def evaluate_postfix(expression: str) -> bool:
    stack = []

    for char in expression:

        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()

            match char:
                case '+': stack.append(a + b)
                case '-': stack.append(a - b)
                case '*': stack.append(a * b)
                case '/': stack.append(a / b)
    return stack.pop()


if __name__ == '__main__':
    expr = input('Enter an expression: ')
    result = evaluate_postfix(expr)
    print(f'Result of Expression: {expr} is {result}')