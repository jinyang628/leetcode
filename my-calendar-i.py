from sortedcontainers import SortedList
class MyCalendar:
    def __init__(self):
        self.start_events = SortedList()
        self.end_events = SortedList()
    def book(self, startTime: int, endTime: int) -> bool:
        left = bisect_right(self.end_events, startTime)
        right = bisect_left(self.start_events, endTime)
        if left != right:
            return False
        self.start_events.add(startTime)
        self.end_events.add(endTime)
        return True
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)