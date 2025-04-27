class MyHashSet:
    def __init__(self):
        self.n = 10000
        self.arr = [[] for _ in range(self.n)]
    def add(self, key: int) -> None:
        bucket = key % self.n
        if key not in self.arr[bucket]:
            self.arr[bucket].append(key)
    def remove(self, key: int) -> None:
        bucket = key % self.n
        if key in self.arr[bucket]:
            self.arr[bucket].remove(key)
    def contains(self, key: int) -> bool:
        bucket = key % self.n
        return key in self.arr[bucket]
# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)