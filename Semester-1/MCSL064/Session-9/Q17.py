from typing import TypeVar

T = TypeVar('T')

class Node:
    def __init__(self, data):
        self.data : T = data
        self.next= None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_beginning(self, data: T) -> None:
        node = Node(data)

        if self.head is None:
            # This is the first node
            self.head = node
            self.tail = node
            self.size += 1
            return

        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1

    def insert_at_end(self, data : T) -> None:
        node = Node(data)

        if self.tail is None:
            self.tail = node
            self.head = node
            self.size += 1
            return

        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1

    def insert_at_location(self, location: int, data: T) -> None:

        if location < 0 or location > self.size:
            print('Location is out of range')
            return

        node = Node(data)

        if self.head is None or location == 0:
            self.insert_at_beginning(data)
            return

        if self.tail is None or location == self.size:
            self.insert_at_end(data)
            return

        # find the middle size
        mid = self.size // 2

        if location <= mid:
            # node to be inserted from beginning to mid. start from beginning
            current_loc = 0
            current_node = self.head
            while current_loc != location:
                current_loc += 1
                current_node = current_node.next

            # found the location, insert the node
            current_node.prev.next = node
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev = node
            self.size += 1

        # node to be inserted from end to mid. start from tail
        elif location > mid:
            current_loc = self.size-1
            current_node = self.tail

            while current_loc != location:
                current_loc -= 1
                current_node = current_node.prev

            # found the location, insert the node
            current_node.prev.next = node
            node.prev = current_node.prev
            node.next = current_node
            current_node.prev = node
            self.size += 1

    def delete_from_beginning(self) -> None:

        if self.head is None:
            print('Linked list is empty')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1

    def delete_from_end(self) -> None:

        if self.tail is None:
            print('Linked list is empty')
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1

    def delete_at_location(self, location: int) -> None:

        if location < 0 or location >= self.size:
            print('Location is out of range')
            return

        if location == 0:
            self.delete_from_beginning()
            return

        if location == self.size-1:
            self.delete_from_end()
            return

        mid = self.size // 2
        if location <= mid:
            # node to be deleted from beginning to mid. start from beginning
            current_loc = 0
            current_node = self.head
            while current_loc != location:
                current_loc += 1
                current_node = current_node.next

            # found the node. delete the node
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size -= 1
        elif location > mid:
            # node to be deleted from mid to end. start from tail
            current_loc = self.size-1
            current_node = self.tail

            while current_loc != location:
                current_loc -= 1
                current_node = current_node.prev

            # found the node. delete the node
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self.size -= 1

    def display(self):

        current_node = self.head
        print('None',end='<->')
        while current_node:
            print(current_node.data, end='<->')
            current_node = current_node.next
        print('None',end='')
        print()

if __name__ == '__main__':
    dl = DoublyLinkedList()
    dl.insert_at_end(1)
    dl.insert_at_end(2)
    dl.insert_at_end(4)
    dl.insert_at_location(2, 3)
    dl.display()  # None<->1<->2<->3<->4<->None
    dl.delete_at_location(2)
    dl.display()  # None<->1<->2<->4<->None
    dl.insert_at_beginning(5)
    dl.display()  # None<->None
