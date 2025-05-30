# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs_inorder(self, root):
        results = []
        
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.val)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(root)
        return results

    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        node_values = self.dfs_inorder(root)

        for i in range(1, len(node_values)):
            if node_values[i] <= node_values[i - 1]:
                return False
        return True
        