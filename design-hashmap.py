class MyHashMap:
    def __init__(self):
        self.track = [None for _ in range(10 ** 7)]
    def put(self, key: int, value: int) -> None:
        self.track[key] = value
    def get(self, key: int) -> int:
        if self.track[key] is not None:
            return self.track[key]
        return -1
    def remove(self, key: int) -> None:
        self.track[key] = None
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)