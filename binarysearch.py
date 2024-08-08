class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []
    
    # Visit the root node first
    result = [root.value]
    
    # Visit the left subtree
    result += preorder_traversal(root.left)
    
    # Visit the right subtree
    result += preorder_traversal(root.right)
    
    return result

def inorder_traversal(root):
    if root is None:
        return []
    
    # Visit the left subtree first
    result = inorder_traversal(root.left)
    
    # Visit the root node
    result.append(root.value)
    
    # Visit the right subtree
    result += inorder_traversal(root.right)
    
    return result

def postorder_traversal(root):
    if root is None:
        return []
    
    # Visit the left subtree first
    result = postorder_traversal(root.left)
    
    # Visit the right subtree
    result += postorder_traversal(root.right)
    
    # Visit the root node
    result.append(root.value)
    
    return result


if __name__ == "__main__":
    

    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(6, TreeNode(5), TreeNode(7))
    
    print("Preorder Traversal:", preorder_traversal(root))
    print("Inorder Traversal:", inorder_traversal(root))
    print("Postorder Traversal:", postorder_traversal(root))
