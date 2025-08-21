class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word

    def starts_with(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True

    def get_words_with_prefix(self, prefix):
        def dfs(node, path, results):
            if node.is_end_of_word:
                # If the current node is the end of a word, add it to the results
                results.append("".join(path))
            # Traverse the children of the current node
            for char, child_node in node.children.items():
                path.append(char)
                dfs(child_node, path, results)
                path.pop()  # Backtrack

        # Start from the node corresponding to the prefix
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []  # No words with the given prefix
            current = current.children[char]

        results = []
        dfs(current, list(prefix), results)
        return results

# Example Usage
trie = Trie()
trie.insert("hello")
trie.insert("help")
trie.insert("heal")
trie.insert("heap")
trie.insert("hero")
trie.insert("hermit")

print(trie.get_words_with_prefix("he"))  # Output: ['hello', 'help', 'heal', 'heap', 'hero', 'hermit']
print(trie.get_words_with_prefix("hel")) # Output: ['hello', 'help']
print(trie.get_words_with_prefix("her")) # Output: ['hero', 'hermit']
print(trie.get_words_with_prefix("ha"))  # Output: [] (no words start with "ha")