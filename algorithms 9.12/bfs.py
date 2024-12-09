from collections import deque

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs(root):
    if root is None:
        return []  
    
    queue = deque([root])  
    values = []  
    
    while queue:
        node = queue.popleft()  
        values.append(node.value) 
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return values

def sum_tree_elements_bfs(root):
    values = bfs(root) 
    return sum(values)  


root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)

print(sum_tree_elements_bfs(root))
