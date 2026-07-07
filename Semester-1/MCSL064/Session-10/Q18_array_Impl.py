class Node:
    def __init__(self, data: int) -> None:
        self.data = data

class BinaryTree:

    def __init__(self) -> None:
        self.children = []

    def add_child(self, data: int) -> None:
        node = Node(data)
        self.children.append(node)

    def print_tree(self):
        if not self.children:
            print('Tree is empty')
            return

        size = len(self.children)
        print(self.children[0].data)

        for i in range(size):
            left_child_index = 2 * i + 1
            if left_child_index >= size:
                break
            print(self.children[left_child_index].data)
            right_child_index = (2 * i) + 2
            if right_child_index >= size:
                break
            print(self.children[right_child_index].data)

if __name__ == '__main__':
    tree = BinaryTree()
    for v in [10,20,30,40,50]:
        tree.add_child(v)

    tree.print_tree()