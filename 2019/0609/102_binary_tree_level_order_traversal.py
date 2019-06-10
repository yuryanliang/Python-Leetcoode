class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Sol:
    def levelOrder(self,root):
        if root is None:
            return []
        result, current =[], [root]
        while current:
            next_level, vals=[], []
            for node in current:
                vals.append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            current=next_level
            result.append(vals)
        return result

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    result = Sol().levelOrder(root)
    print result