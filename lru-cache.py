class Node:
    def __init__(self, key: int, val: int, prev: Optional["Node"] = None, next: Optional["Node"] = None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.track = {} # key is the key, value is a pointer to the Node
        self.oldest = Node(0, 0)
        self.youngest = Node(0, 0)        
        self.oldest.next = self.youngest
        self.youngest.prev = self.oldest
    def get(self, key: int) -> int:
        if key in self.track:
            self.remove(self.track[key])
            self.insert(self.track[key])
            return self.track[key].val
        return -1
    def insert(self, node: Node):
        prev_youngest = self.youngest.prev
        prev_youngest.next = node
        self.youngest.prev = node
        node.next = self.youngest 
        node.prev = prev_youngest
    def remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    def put(self, key: int, value: int) -> None:
        if key in self.track:
            self.remove(self.track[key])
        self.track[key] = Node(key, value)
        self.insert(self.track[key])
        if len(self.track) > self.capacity:
            oldest = self.oldest.next 
            self.remove(oldest)
            del self.track[oldest.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)