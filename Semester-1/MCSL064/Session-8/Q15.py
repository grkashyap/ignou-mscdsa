from typing import TypeVar

T = TypeVar('T')

class QueueTwoStacks:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element: T) -> None:
        self.stack1.append(element)
        self.__print_queue()

    def dequeue(self) -> T | None:

        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print('Queue is empty!')
            return None

        if not self.stack2:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        val = self.stack2.pop()
        self.__print_queue()
        return val

    def peek(self) -> T | None:

        if len(self.stack1) == 0 and len(self.stack2) == 0:
            print('Queue is empty!')
            return None

        if not self.stack2:
            while len(self.stack1) != 0:
                self.stack2.append(self.stack1.pop())

        val = self.stack2[-1]
        self.__print_queue()
        return val

    def __print_queue(self) -> None:
        print('Printing Stack1: ')
        for elem in self.stack1:
            print(elem, end=' ')
        print()

        print('Printing Stack2: ')
        for elem in self.stack2:
            print(elem, end=' ')
        print()

if __name__ == '__main__':
    queue = QueueTwoStacks()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print('Removed element: ', queue.dequeue())
    queue.enqueue(4)
    queue.enqueue(5)
    print('Last element: ', queue.peek())