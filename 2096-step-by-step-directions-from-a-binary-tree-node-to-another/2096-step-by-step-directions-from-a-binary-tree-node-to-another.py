# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def dfs(node, path, target):
            if not node:
                return False

            if node.val == target:
                return True
                    
            if dfs(node.left, path, target):
                path.append("L")
                return True
            
            if dfs(node.right, path, target):
                path.append("R")
                return True
            return False
        
        path_start = []
        path_dest = []
        dfs(root, path_start, startValue)
        dfs(root, path_dest, destValue)


        path_start = path_start[::-1]
        path_dest = path_dest[::-1]

        i = 0
        while i < len(path_start) and i < len(path_dest) and path_start[i] == path_dest[i]:
            i += 1

        res = 'U' *  (len(path_start) - i )     
        
        res += ''.join(path_dest[i:])        
        return res

