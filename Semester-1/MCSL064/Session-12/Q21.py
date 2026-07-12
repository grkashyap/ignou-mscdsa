class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data: int) -> None:
        node = Node(data)

        if self.root is None:
            self.root = node
            return

        current_node = self.root

        while current_node is not None:
            if current_node.data > data and current_node.left is not None:
                current_node = current_node.left
            elif current_node.data < data and current_node.right is not None:
                current_node = current_node.right
            else:
                break
        else:
            return

        if current_node.data > data:
            current_node.left = node
        elif current_node.data < data:
            current_node.right = node

    def delete(self, root : Node | None, data: int) -> Node | None:
        if root is None:
            return root

        if root.data > data:
            # value to be deleted is less than current node. Check in left subtree
            root.left = self.delete(root.left, data)
        elif root.data < data:
            # value to be deleted is greater than current node. Check in right subtree
            root.right = self.delete(root.right, data)
        else:
            # found the node to be deleted
            # if the node has 0 or 1 children
            if root.left is None:
                return root.right
            if root.right is None:
                return root.left

            # if the node has 2 children
            successor = self.__get_successor(root)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)

        return root

    def __get_successor(self, root: Node) -> Node | None:
        # find the smallest node in the right subtree
        current_node = root.right
        while current_node is not None and current_node.left is not None:
            current_node = current_node.left
        return current_node

    def search(self, root: Node, data:int) -> bool:
        if root is None:
            return False

        while root is not None:
            if root.data == data:
                return True
            elif root.data < data:
                root = root.right
            else:
                root = root.left

        return False

if __name__ == '__main__':
    bst = BinarySearchTree()
    for i in [50,30,70,20,40]:
        bst.insert(i)

    print('10 is present in the Binary Search Tree: ',bst.search(bst.root, 10))
    print('20 is present in the Binary Search Tree: ', bst.search(bst.root, 20))

    print('Deleting 20 from the search tree')
    bst.root = bst.delete(bst.root, 20)

    print('20 is present in the Binary Search Tree: ', bst.search(bst.root, 20))