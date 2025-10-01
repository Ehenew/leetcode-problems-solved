class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert(word)

        n = len(s)

        def dfs(idx):
            if idx == n:
                return True
            
            node = trie.root
            for i in range(idx, n):
                ch = s[i]
                if ch not in node.children:
                    break
                node = node.children[ch]
                if node.is_end:  # found a word
                    if dfs(i + 1):   # break the rest
                        return True
            return False
        return dfs(0)

