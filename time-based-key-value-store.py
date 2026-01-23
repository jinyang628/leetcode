1class TimeMap:
23    def __init__(self):
4        self.tracker = defaultdict(list) # key is the key, value is (timestamp, value)
56    def set(self, key: str, value: str, timestamp: int) -> None:
7        self.tracker[key].append((timestamp, value))
89    def get(self, key: str, timestamp: int) -> str:
10        values = self.tracker[key]
11        if not values:
12            return ""
13        left, right = 0, len(values) - 1
14        best_possible_value = ""
15        while left <= right:
16            mid = left + (right - left) // 2
17            if values[mid][0] <= timestamp:
18                best_possible_value = values[mid][1]
19                left = mid + 1
20            else:
21                right = mid - 1
22        return best_possible_value
232425# Your TimeMap object will be instantiated and called as such:
26# obj = TimeMap()
27# obj.set(key,value,timestamp)
28# param_2 = obj.get(key,timestamp)