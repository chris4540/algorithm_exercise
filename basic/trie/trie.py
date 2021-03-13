"""
Implementation exercise of the data structure "Tries"
In DS and algo in python, it is called standard tries
https://albertauyeung.github.io/2020/06/15/python-trie.html

https://www.geeksforgeeks.org/trie-insert-and-search/
"""
from typing import Dict


class TrieNode:
    char: str
    children: Dict[str, "TrieNode"]

    def __init__(self, char: str):
        self.char = char

        self.children = {}
        self.parent = None
        self.counter = 0
        self.is_end = False


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
                # if not, create a new one
                new_node = TrieNode(c)
                node.children[c] = new_node
                new_node.parent = node
                node = new_node
        node.is_end = True
        node.counter += 1

    def search(self, string: str):

        node = self.root
        ret = []
        # match the candidates
        for c in string:
            if c in node.children:
                # traverse
                node = node.children[c]
            else:
                # we cannot match the search string as a prefix, return empty list
                return ret

        # till this point, we can search the stored words in the trie in DFS manner
        stack = [node]
        prefix = string
        while stack:
            node = stack.pop() # pop the last one

            # visiting
            prefix += node.char
            if node.is_end:
                word = self.get_word(node)
                ret.append((word, node.counter))

            if node.children:
                for n in node.children.values():
                    stack.append(n)

        return ret

    def get_word(self, node):
        """ Backtrace the current node the root in order to get the word
        """
        node_ = node
        ret = ""
        while node_.parent:
            ret = node_.char + ret
            node_ = node_.parent

        return ret

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
    t.insert("who")
    t.insert("where")
    t.insert("what")
    print(t.search("wh"))
    # t.print_nodes()
