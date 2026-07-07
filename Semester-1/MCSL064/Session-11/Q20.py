from collections import deque

class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.num_nodes = 0

    def insert(self, data: int) -> None:
        node = Node(data)
        if self.root is None:
            self.root = node
            self.num_nodes += 1
            return

        nodes = deque()
        nodes.append(self.root)
        while nodes:
            current_node = nodes.popleft()

            if current_node.left is None:
                current_node.left = node
                self.num_nodes += 1
                return
            nodes.append(current_node.left)

            if current_node.right is None:
                current_node.right = node
                self.num_nodes += 1
                return
            nodes.append(current_node.right)

    def preorder_traversal(self):
        if self.root:
            nodes: list[Node] = [self.root]
            while nodes:
                current_node = nodes.pop()
                print(current_node.data, end=" ")
                if current_node.right is not None:
                    nodes.append(current_node.right)
                if current_node.left is not None:
                    nodes.append(current_node.left)

    def inorder_traversal(self):
        if self.root:
            current_node = self.root
            nodes = []
            while current_node is not None or nodes:

                while current_node is not None:
                    nodes.append(current_node)
                    current_node = current_node.left

                current_node = nodes.pop()
                print(current_node.data, end=" ")
                current_node = current_node.right

    def postorder_traversal(self):
        if self.root:
            nodes1: list[Node] = [self.root]
            nodes2: list[Node] = []

            while nodes1:
                current_node = nodes1.pop()
                nodes2.append(current_node)

                if current_node.left is not None:
                    nodes1.append(current_node.left)

                if current_node.right is not None:
                    nodes1.append(current_node.right)

            while nodes2:
                print(nodes2.pop().data, end=" ")


if __name__ == '__main__':
    tree = BinaryTree()
    for v in [10,20,30,40,50]:
        tree.insert(v)

    print('Preorder Traversal')
    tree.preorder_traversal()
    print()

    print('Inorder Traversal')
    tree.inorder_traversal()
    print()

    print('Postorder Traversal')
    tree.postorder_traversal()

