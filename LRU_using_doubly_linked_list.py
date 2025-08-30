# Python program to implement LRU Least Recently Used)
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add(self, node: Node):
      
        # Add a node right after the head
        # (most recently used position).
        next_node = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next_node
        next_node.prev = node

    def _remove(self, node: Node):
      
       # remove a node from the
        # doubly linked list.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        # Get the value for a given key
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._remove(node)cccccbvrfnfbnjg
        self._add(node)
        return node.value

    def put(self, key: int, value: int):
      
        #Put a key-value pair into the cache.
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            del self.cache[key]

        if len(self.cache) >= self.capacity:
          
            # Remove the least recently used item
            # (just before the tail)
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

        # Add the new node
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node


if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))