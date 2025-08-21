class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False  # True if the node represents the end of a word.

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                # If the character is not present, add a new TrieNode
                current.children[char] = TrieNode()
            current = current.children[char]
        # Mark the last node as the end of a word
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            # Check if character exists in the trie
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word  # Return True only if it's the end of a word

# Example Usage
trie = Trie()
trie.insert("hello")
trie.insert("world")

print(trie.search("hello"))  # Output: True
print(trie.search("world"))  # Output: True
print(trie.search("help"))   # Output: False