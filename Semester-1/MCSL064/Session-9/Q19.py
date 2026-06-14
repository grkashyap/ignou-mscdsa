class Node:
    def __init__(self, val) -> None:
        self.val: int = val
        self.next: Node | None = None

class SingleLinkedList:
    """
    Operations:
        - Insert at the beginning
        - Insert at specific location
        - Insert at the end
        - Remove first node
        - Remove last node
        - Remove at specific location
        - Traversal
    """
    def __init__(self) -> None:
        self.head: Node | None = None

    def insert_at_beginning(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            # This is the first node
            self.head = node
            return

        node.next = self.head
        self.head = node
        return

    def insert_at_end(self, val: int) -> None:
        node = Node(val)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = node
        return

    def insert_at_location(self, val: int, location: int) -> None:
        if location == 0:
            self.insert_at_beginning(val)
            return

        if location == -1:
            self.insert_at_end(val)
            return

        node = Node(val)
        current_loc = 0
        current = self.head
        prev = None

        while current_loc < location and current is not None:
            current_loc += 1
            prev = current
            current = current.next

        if current is None or current_loc != location:
            print('Invalid location')
            return

        prev.next = node
        node.next = current
        return

    def remove_from_start(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        self.head = self.head.next
        return

    def remove_from_end(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        prev = None

        while current.next is not None:
            prev = current
            current = current.next

        prev.next = None
        return

    def remove_from_location(self, location: int) -> None:
        if location == 0:
            self.remove_from_start()
            return

        if location == -1:
            self.remove_from_end()
            return

        current_loc = 0
        current = self.head
        prev = None

        while current_loc < location and current is not None:
            current_loc += 1
            prev = current
            current = current.next

        if current is None or current_loc != location:
            print('Invalid location')
            return

        prev.next = current.next
        return

    def traverse_list(self) -> None:
        if self.head is None:
            print("Linked list is empty")
            return

        current = self.head
        while current is not None:
            print(current.val, end=' ')
            current = current.next
        print()

if __name__ == '__main__':
    lst = SingleLinkedList()

    # Empty list operations
    lst.remove_from_start()
    lst.remove_from_end()

    # Single node
    lst.insert_at_end(1)
    lst.remove_from_end()

    # Insert at beginning
    lst.insert_at_end(1)
    lst.insert_at_end(2)
    lst.insert_at_beginning(0)
    lst.traverse_list()  # 0 1 2

    # Invalid locations
    lst.insert_at_location(5, 100)
    lst.traverse_list()
    lst.remove_from_location(100)