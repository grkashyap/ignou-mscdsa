class Node:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data: int) -> None:
        node = Node(data)
        if not self.root:
            self.root = node
            return

        nodes = [self.root]

        while nodes:
            current_node = nodes.pop(0)

            if current_node.left is None:
                current_node.left = node
                return
            nodes.append(current_node.left)

            if current_node.right is None:
                current_node.right = node
                return
            nodes.append(current_node.right)

    def inorder_traversal(self, node: Node) -> None:
        """
            Inorder Traversal:
            Left -> Node -> Right
        """
        if node:
           self.inorder_traversal(node.left)
           print(node.data, end=" ")
           self.inorder_traversal(node.right)

    def preorder_traversal(self, node: Node) -> None:
        """
            Preorder Traversal:
            Node -> left -> Right
        """
        if node:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def postorder_traversal(self, node: Node) -> None:
        """
            Postorder Traversal:
            Left -> Right -> Node
        """
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

if __name__ == '__main__':
    tree = BinaryTree()
    for v in [10,20,30,40,50]:
        tree.insert(v)

    print('Preorder Traversal')
    tree.preorder_traversal(tree.root)

    print()
    print('Inorder Traversal')
    tree.inorder_traversal(tree.root)

    print()
    print('Postorder Traversal')
    tree.postorder_traversal(tree.root)