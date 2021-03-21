"""
https://leetcode.com/problems/lru-cache/

https://www.interviewcake.com/concept/java/lru-cache

Notes:
Use double linked list to track the order of access => All O(1) operation\
Use hashmap to map key to the node
"""

from typing import Dict

class DoubleLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._map: Dict[int, DoubleLinkedNode] = {}

        # use double linked list for saving
        self._head = DoubleLinkedNode()
        self._tail = DoubleLinkedNode()
        self._head.next = self._tail
        self._tail.prev = self._head


    def get(self, key: int) -> int:
        if key in self._map:
            node = self._map[key]
            # remove from the linked list
            self._remove_node(node)
            # put it after head
            self._add_node(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._remove_node(self._map[key])

        node = DoubleLinkedNode(key, value)
        self._map[key] = node
        self._add_node(node)

        if len(self._map) > self.capacity:
            # remove the node = tail.prev
            self._map.pop(self._tail.prev.key)
            self._remove_node(self._tail.prev)

        assert len(self._map) <= self.capacity


    def _add_node(self, node: DoubleLinkedNode):
        tmp = self._head.next
        # handle self._head <---> node
        self._head.next = node
        node.prev = self._head

        # handle node <---> tmp
        node.next = tmp
        tmp.prev = node

    def _remove_node(self, node: DoubleLinkedNode):
        prev_ = node.prev
        next_ = node.next
        prev_.next = next_
        next_.prev = prev_

if __name__ == '__main__':
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)
    lru_cache.put(2, 2)
    assert lru_cache.get(1) == 1
    lru_cache.put(3, 3)
    assert lru_cache.get(2) == -1
    lru_cache.put(4, 4)
    assert lru_cache.get(1) == -1
    assert lru_cache.get(3) == 3
    assert lru_cache.get(4) == 4