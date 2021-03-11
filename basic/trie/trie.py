"""
Implementation exercise of the data structure "Tries"
https://albertauyeung.github.io/2020/06/15/python-trie.html
"""
from typing import Dict


class TrieNode:
    char: str
    children: Dict[str, "TrieNode"]

    def __init__(self, char: str):
        self.char = char

        self.children = {}
        self.counter = 0


class Trie:
    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str):
        node = self.root
        for c in word:
            if c in node.children:
                # traverse to the existing char node
                node = node.children[c]
            else:
                # if not
                new_node = TrieNode(c)
                node.children[c] = new_node
                node = new_node
        node.is_end = True
        node.counter += 1

    def query(self):
        pass

    def print_nodes(self):
        nodes = [self.root]

        # BFS
        while nodes:
            node = nodes.pop(0)
            for child_node in node.children.values():
                nodes.append(child_node)

            print(node.char, end=' ')

        print("")


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    t.print_nodes()
