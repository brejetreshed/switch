class BinaryTree:

    def __init__(self, data):
        self.data = data 
        self.left = None  #left child
        self.right = None  #right child

    def add_left(self, child_node):
        self.left = child_node

    def add_right(self, child_node):
        self.right = child_node

#left,root,right
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data)
        in_order_traversal(node.right)

#root,left,right
def pre_order_traversal(node):
    if node:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

#left,right,root
def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)


def find_max_value(node):
    if node is None:
        return float('-inf')  # Return negative infinity for empty nodes

    # Recursively find the maximum in the left and right subtrees
    left_max = find_max_value(node.left)
    right_max = find_max_value(node.right)

    return max(node.data, left_max, right_max)




root = BinaryTree(10)
root.add_left(BinaryTree(20))
root.add_right(BinaryTree(30))
root.left.add_left(BinaryTree(70))
root.left.add_right(BinaryTree(50))
root.right.add_left(BinaryTree(60))

print(find_max_value(root))

root.left.add_right(BinaryTree(100))
root.right.add_left(BinaryTree(60))
print(find_max_value(root))
