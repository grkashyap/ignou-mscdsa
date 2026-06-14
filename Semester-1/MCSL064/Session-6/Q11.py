from typing import TypeVar

T = TypeVar('T')

class Stack:

    def __init__(self) -> None:
        self.items = [T]
        self.size = 0

    def push(self, item: T) -> None:
        if self.size >= len(self.items):
            self.items.append(item)
        else:
            self.items[self.size] = item

        self.size += 1

    def pop(self) -> T:
        if self.size == 0:
            print('Stack is empty')
            return None

        val = self.items[self.size]
        return val

    def peek(self) -> T:
        if self.size == 0:
            print('Stack is empty')
            return None

        return self.items[self.size-1]

    def print(self) -> None:
        for item in self.items:
            print(item, end=' ')
        print()


if __name__ == '__main__':
    print('Stack Operations.')
    stack = Stack()
    while True:
        print('Select Stack Operation: ')
        print('1: Push')
        print('2: Pop')
        print('3: Peek')
        print('4: Print')
        print('5: exit')

        operation = int(input('Enter your choice: '))

        if operation == 5:
            break
        elif operation == 1:
            value = input('Enter value to be inserted into stack: ')
            stack.push(value)
        elif operation == 2:
            print(f'Removing value at the top of the stack and returning: {stack.pop()}')
        elif operation == 3:
            print(f'Returning value at the top of the stack without removing: {stack.peek()}')
        else:
            print('Values in the stack')
            stack.print()