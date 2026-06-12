class LRUCache:

    class Node:

        def __init__(self, key: int, value: int, prev: Node = None, next: Node = None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)
        self.cache = {}

        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_tail(self, node: Node):
        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node
        
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]

        self._remove(node)
        self._add_to_tail(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        
        node = self.Node(key, value)
        self.cache[key] = node
        self._add_to_tail(node)

        if len(self.cache) > self.capacity:
            oldest = self.head.next
            self._remove(oldest)
            del self.cache[oldest.key]