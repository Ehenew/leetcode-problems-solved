class TrieNode:
    def __init__(self):
        self.children = {}
        self._sum = 0

class MapSum:
    def __init__(self):
        self.root = TrieNode()
        self.key_val = {}   

    def insert(self, key: str, val: int) -> None:
        diff = val - self.key_val.get(key, 0)
        self.key_val[key] = val

        node = self.root
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node._sum += diff

    def sum(self, prefix: str) -> int:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node._sum
