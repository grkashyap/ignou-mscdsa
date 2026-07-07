class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data) -> None:
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            # if the left child is empty
            if not current_node.left:
                current_node.left = node
                return
            queue.append(current_node.left)

            # if the right child is empty
            if not current_node.right:
               current_node.right = node
               return
            queue.append(current_node.right)

        return self.root

    def print_tree(self, node) -> None:
        if node:
            print(node.data, end=' ')
            self.print_tree(node.left)
            self.print_tree(node.right)

if __name__ == '__main__':
    tree = BinaryTree()
    for v in [10,20,30,40,50]:
        tree.insert(v)

    root = tree.root
    tree.print_tree(root)
