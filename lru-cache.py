class Node:
    def __init__(self, key: int, val: int, prev_node: Optional["Node"] = None, next_node: Optional["Node"] = None):
        self.key = key
        self.val = val
        self.prev_node = prev_node
        self.next_node = next_node
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next_node = self.latest
        self.latest.prev_node = self.oldest
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.delete(node)
            self.insert(node)
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.insert(Node(key, value))
        if len(self.cache) > self.capacity:
            self.delete(self.oldest.next_node)
    def insert(self, node: Node) -> None:
        prev, next_node = self.latest.prev_node, self.latest
        prev.next_node = node
        node.prev_node = prev
        node.next_node = next_node
        next_node.prev_node = node 
        self.cache[node.key] = node
    def delete(self, node: Node) -> None:
        prev, next_node = node.prev_node, node.next_node
        prev.next_node = next_node
        next_node.prev_node = prev
        del self.cache[node.key]
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)