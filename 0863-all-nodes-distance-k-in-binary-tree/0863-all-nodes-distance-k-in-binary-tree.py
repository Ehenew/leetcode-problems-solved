
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque, defaultdict

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent = {}

        def dfs(node, p=None):
            if not node:
                return
            parent[node] = p
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root)

        q = deque([(target, 0)])
        visited = set([target])

        res = []
        while q:
            node, dist = q.popleft()

            if dist == k:
                res.append(node.val)

            for neighbor in (node.left, node.right, parent[node]):
                if neighbor and neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dist + 1))

        return res
