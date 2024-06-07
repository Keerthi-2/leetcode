class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for c in word:
            if current.children[ord(c) - ord("a")] is None:
                current.children[ord(c) - ord("a")] = TrieNode()
            current = current.children[ord(c) - ord("a")]
        current.isEnd = True

    # Find the shortest root of the word in the trie
    def shortest_root(self,word):
        cur=self.root
        for i in range(len(word)):
            c=word[i]
            if cur.children[ord(c)-97]==None:
                return word
            
            cur=cur.children[ord(c)-97]
            if cur.isEnd:
                return word[:i+1]
        
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        word_array = sentence.split()

        dict_trie = Trie()
        for word in dictionary:
            dict_trie.insert(word)

        # Replace each word in the sentence with the corresponding shortest root
        for word in range(len(word_array)):
            word_array[word] = dict_trie.shortest_root(word_array[word])

        return " ".join(word_array)