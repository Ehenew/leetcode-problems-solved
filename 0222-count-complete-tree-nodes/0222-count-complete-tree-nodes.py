class Solution:
    def countNodes(self, root):
        def get_left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        
        def get_right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        
        if not root:
            return 0
        
        lh = get_left_height(root)
        rh = get_right_height(root)
        
        if lh == rh:
            return (1 << lh) - 1        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)