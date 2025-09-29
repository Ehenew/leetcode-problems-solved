class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> str:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]            
        return node.is_end


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        longest_word = ""

        def dfs(node, path):
            nonlocal longest_word
            if node != trie.root and not node.is_end:
                return
            if len(path) > len(longest_word):
                longest_word = path
            
            for ch in sorted(node.children.keys()):  
                dfs(node.children[ch], path + ch)

        dfs(trie.root, "")
        return longest_word