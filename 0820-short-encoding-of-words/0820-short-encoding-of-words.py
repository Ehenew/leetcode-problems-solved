class TrieNode:
    def __init__(self):
        self.children = {}

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = list(set(words))
        words = [w[::-1] for w in words]

        root = TrieNode()
        nodes = {}  

        for w in words:
            cur = root
            for ch in w:
                if ch not in cur.children:
                    cur.children[ch] = TrieNode()
                cur = cur.children[ch]
            nodes[cur] = len(w) + 1 
             
        return sum(val for node, val in nodes.items() if not node.children)

