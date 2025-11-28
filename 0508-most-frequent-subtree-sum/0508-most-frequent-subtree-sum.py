# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = {}  
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            s = node.val + left + right

            freq[s] = freq.get(s, 0) + 1
            max_freq = max(max_freq, freq[s])
            return s
        dfs(root)
        return [s for s, c in freq.items() if c == max_freq]