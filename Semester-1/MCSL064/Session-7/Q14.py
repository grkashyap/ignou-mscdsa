"""
Double ended queue or dequeue supports adding/removing elements from both sides i.e. front and back.
Operations Supported -
 - Append - Add element at the back of the queue
 - AppendLeft - Adding element to the front of the queue
 - Pop - Remove element from the back of the queue
 - PopLeft - Removing element from the front of the queue
 - Peek - Retrieve the front or back element of the queue without removing it

"""
from typing import TypeVar

T = TypeVar('T')

class Dequeue:

    def __init__(self):
        self.queue = []
        self.size = 0

    def append(self, element: T) -> T:
        self.queue.append(element)
        self.size += 1
        dequeue.print()
        return element

    def appendLeft(self, element: T) -> T:
        self.queue.insert(0, element)
        self.size -= 1
        dequeue.print()
        return element

    def pop(self) -> T | None:
        if self.__is_queue_empty():
            print("Dequeue is empty!")
            return None

        val = self.queue.pop(self.size-1)
        dequeue.print()
        return val

    def popLeft(self) -> T | None:
        if self.__is_queue_empty():
            print("Dequeue is empty!")
            return None

        val = self.queue.pop()
        dequeue.print()
        return val

    def peek(self) -> tuple | None:
        if self.__is_queue_empty():
            print("Dequeue is empty!")
            return None

        return self.queue[0], self.queue[-1]

    def print(self) -> None:
        print("Elements in Dequeue:")
        for elem in self.queue:
            print(elem, end=' ')
        print()

    def __is_queue_empty(self) -> bool:
        return self.size == 0

if __name__ == '__main__':
    dequeue = Dequeue()
    print(dequeue.peek())
    print('Adding elements to Dequeue: ')
    dequeue.append(1)
    dequeue.appendLeft(2)
    dequeue.append(3)
    print('Peeking elements from Dequeue: ',dequeue.peek())
    print('Removing elements from Dequeue: ')
    dequeue.pop()
    dequeue.popLeft()