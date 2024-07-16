from queue import Queue

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = Queue()
    queue.put(root)
    
    while not queue.empty():
        level = []
        level_size = queue.qsize()
        
        for _ in range(level_size):
            node = queue.get()
            level.append(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
        result.append(level)
    
    return result

# Example usage
# Constructing a binary tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

print(level_order_traversal(root))