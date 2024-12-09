class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(root):
    stack = [root]
    visited = []
    while stack:
        node = stack.pop()
        if node:
            visited.append(node.value) 
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return visited

def sum_elements(root):
    values = dfs(root)  
    return sum(values)  

# Example Usage
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)

print(sum_elements(root))
