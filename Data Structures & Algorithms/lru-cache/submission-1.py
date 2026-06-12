class LRUCache:

    class Node:

        def __init__(self, key: int, value: int, prev: Node, next: Node):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None
        self.tail = None
        self.cache = {}
        
    def get(self, key: int) -> int:
        node = self.cache.get(key)

        if not node:
            return -1
        
        self.manageOrder(node)
        
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.value = value
            self.manageOrder(node)
        else:
            node = self.Node(key, value, None, None)
            self.cache[key] = node
            
            if self.size == 0:
                self.head = node
                self.tail = node
                self.size = 1
            elif self.size < self.capacity:
                self.moveToEnd(node)
                self.size += 1
            else: # size >= capacity
                del self.cache[self.head.key]
                self.moveToEnd(node)
                self.head.next.prev = None
                self.head = self.head.next

    def manageOrder(self, node: Node):
        if node.prev is None and node.next: 
            node.next.prev = None
            self.head = node.next
        elif node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        # Other combinations means node is alone or node is last to remove anyways

        if node != self.tail:
            self.moveToEnd(node)

    def moveToEnd(self, node: Node):
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        node.next = None
        
