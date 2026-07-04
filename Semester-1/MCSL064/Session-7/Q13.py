from typing import TypeVar

T = TypeVar('T')

class Queue:

    def __init__(self):
        self.queue: T = []
        self.size: int = 0

    def enqueue(self, element: T) -> None:
        self.queue.append(element)
        self.size += 1

    def dequeue(self) -> T:
        if self.size == 0:
            print('Queue is empty!')
            return None

        self.size -= 1
        return self.queue.pop(0)

if __name__ == '__main__':
    queue = Queue()
    print('Adding values to Queue')
    queue.enqueue('a')
    queue.enqueue('b')
    queue.enqueue('c')
    print('Removing values from Queue')
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())